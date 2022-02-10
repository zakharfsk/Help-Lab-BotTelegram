import uuid
import logging
import psycopg2

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from create_bot import bot
from config import USER, HOST, DATABASE, PASSWORD, OWNER, select_object_buttons, CHAT
from create_keyboards.keyboards import subject_keyboard, start_menu

username = USER
host = HOST
database = DATABASE
password = PASSWORD
port = 5432


class Order(StatesGroup):
    waiting_subject = State()
    waiting_input_files = State()
    waiting_input_group = State()
    waiting_input_tasks = State()


async def start_order_english(message: types.Message, state: FSMContext):
    try:
        await state.update_data(customer_id = message.from_user.id, order_id = int(uuid.uuid4().fields[-1]))
        await Order.waiting_subject.set()
        await message.reply('Виберіть предмет.', reply_markup = subject_keyboard(select_object_buttons).add('Отмена'))
    except Exception as e:
        logging.exception(e)


async def cancel_order(message: types.Message, state: FSMContext):
    try:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.reset_state(with_data = True)

        await message.reply(
            'Вихід з створення заказу\n'\
            'Вас перенаправлено в головне меню',
            reply_markup = start_menu()
        )

    except Exception as e:
        logging.exception(e)


async def input_subject(message: types.Message, state: FSMContext):
    try:
        subject = message.text
        if subject in select_object_buttons:
            await state.update_data(select_object=subject)
            await Order.next()
            await message.reply(
                'Надішліть мені файл з завданнями, будь ласка ^^',
                reply_markup = types.ReplyKeyboardMarkup(resize_keyboard = True).add('Отмена')
            )
        else:
            await message.reply(
                'Упсс...\n' \
                'Нажаль такого предмета немає'
            )
    except Exception as e:
        logging.exception(e)


async def input_files(message: types.Message, state: FSMContext):
    try:
        await state.update_data(files = message.document.file_id)
        await message.answer('Вкажіть вашу групу.(в форматі КІ-21-1)',
                             reply_markup = types.ReplyKeyboardMarkup(resize_keyboard = True).add('Отмена'))
        await Order.next()

    except Exception as e:
        logging.exception(e)


async def input_group(message: types.Message, state: FSMContext):
    try:
        group = message.text
        await state.update_data(user_group = group)

        await message.answer('Опишіть що потрібно зробити.',
                             reply_markup = types.ReplyKeyboardMarkup(resize_keyboard = True).add('Отмена'))
        await Order.next()

    except Exception as e:
        logging.exception(e)


async def input_task(message: types.Message, state: FSMContext):
    try:
        tasks = message.text
        payments: types.ChatMember = await bot.get_chat_member(OWNER, OWNER)
        await state.update_data(task = tasks)

        data = await state.get_data()

        await message.answer(f'{data}')

        conn = psycopg2.connect(
            user = username,
            host = host,
            database = database,
            password = password,
            port = port
        )
        cursor = conn.cursor()

        if message.from_user.id != OWNER:
            cursor.execute(
                'INSERT INTO public.order_info_english(id_order, id_customer, name_object, user_group, file_id, task) '\
                f'VALUES ({data["order_id"]}, {data["customer_id"]}, \'{data["select_object"]}\', \'{data["user_group"]}\', \'{data["files"]}\', \'{data["task"]}\');'
            )
            conn.commit()

        await message.reply(
            'Дякуємо за замовлення. Скоро звами зв\'яжуться наші менеджери',
            reply_markup = start_menu()
        )

        await message.answer(
            'Ваш чек.\n\n'
            f'ID заказа: {data["order_id"]}\n' \
            f'ID замовника: {data["customer_id"]}\n' \
            f'Username: {message.from_user.username}\n' \
            f'First Name: {message.from_user.first_name}\n' \
            f'Last Name: {message.from_user.last_name}\n' \
            f'Предмет: {data["select_object"]}\n' \
            f'Група: {data["user_group"]}\n' \
            f'Завдання: {data["task"]}\n\n' \
            'Час виконання: 1-2 дня\n' \
            f'Щоб оплатити зверніться до {payments.user.mention}\n\n'\
            f'Файл який ви надіслали:'
        )

        await bot.send_document(message.from_user.id, data['files'])

        await bot.send_message(
            CHAT,
            f'ID заказа: {data["order_id"]}\n' \
            f'ID замовника: {data["customer_id"]}\n' \
            f'Username: {message.from_user.username}\n' \
            f'First Name: {message.from_user.first_name}\n' \
            f'Last Name: {message.from_user.last_name}\n' \
            f'Предмет: {data["select_object"]}\n' \
            f'Група: {data["user_group"]}\n' \
            f'Завдання: {data["task"]}\n\n' \
        )

        await bot.send_document(
            CHAT,
            data['files']
        )

        await state.reset_state(with_data = True)

    except Exception as e:
        logging.exception(e)


def register_message_handler_create_order_english(dp: Dispatcher):
    try:
        dp.register_message_handler(start_order_english, Text(equals='💸 Зробити замовлення'), state = None)
        dp.register_message_handler(cancel_order, state = "*", commands = ['back'])
        dp.register_message_handler(cancel_order, Text(equals = 'Отмена'), state = "*")
        dp.register_message_handler(input_subject, Text(equals = 'Англійська мова'),
                                    state = Order.waiting_subject)
        dp.register_message_handler(input_files, content_types = types.ContentTypes.DOCUMENT,
                                    state = Order.waiting_input_files)
        dp.register_message_handler(input_group, state = Order.waiting_input_group)
        dp.register_message_handler(input_task, state = Order.waiting_input_tasks)
    except Exception as e:
        logging.exception(e)
