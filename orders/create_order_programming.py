import aiogram
import uuid
import logging
import psycopg2
import json

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from create_bot import dp, bot
from config import USER, HOST, DATABASE, PASSWORD, OWNER, CHAT, labaratories_buttons, \
    select_object_buttons
from create_keyboards.keyboards import subject_keyboard, labaratories_keyboard, start_menu, cancel_keyboard

username = USER
host = HOST
database = DATABASE
password = PASSWORD
port = 5432

class Order(StatesGroup):
    waiting_subject = State()
    waiting_number_lab = State()
    waiting_variant = State()
    waiting_zvit = State()
    waiting_count_task = State()

async def start_order(message: types.Message, state: FSMContext):
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
            await state.update_data(select_object = subject)
            await Order.next()
            await message.reply('Виберіть Лабораторну.', reply_markup = labaratories_keyboard().add('Отмена'))
        else:
            await message.reply(
                'Упсс...\n'\
                'Нажаль такого предмета немає'
            )
    except Exception as e:
        logging.exception(e)

async def input_number_lab(message: types.Message, state: FSMContext):
    try:
        num_lab = message.text

        if num_lab in labaratories_buttons:
            await state.update_data(number_lab = num_lab)
            await message.reply('Вкажіть номер вашого варіанта.', reply_markup = cancel_keyboard())
            await Order.next()
        else:
            await message.reply(
                'Упс...\n'
                'Нажаль в нас немає такої лабораторної'
            )
    except Exception as e:
        logging.exception(e)

async def input_lab_variant(message: types.Message, state: FSMContext):
    try:
        try:
            variant = message.text
            await state.update_data(variant_lab = int(variant))
            await Order.next()
            await message.reply(
                'Виберіть кількість завдань( ціну можна подивитися в прайсі до лабораторної )\n'\
                '<code>Увага! Якщо ви вкажете не коректно кількість завдань, то цей заказ не буде розглядатися.</code>',
                reply_markup = cancel_keyboard()
            )
        except ValueError:
            await message.reply('Номер варіанта має бути числом.')
    except Exception as e:
        logging.exception(e)

async def input_task(message: types.Message, state: FSMContext):
    try:
        try:
            task = message.text
            await state.update_data(task = int(task))
            await Order.next()
            await message.reply(
                'Якщо Ви хочете з звітами то напишіть <b>+</b>, якщо без звітів то напишіть <b>-</b>',
                reply_markup=cancel_keyboard()
            )
        except ValueError:
            await message.reply('Кількість завданнь має бути числом.')
    except Exception as e:
        logging.exception(e)

async def input_zvit(message: types.Message, state: FSMContext):
    try:

        with open('data/all_price/price_programming.json', 'r') as f:
            price = json.load(f)

        conn = psycopg2.connect(
            user = username,
            host = host,
            database = database,
            password = password,
            port = port
        )

        cursor = conn.cursor()

        z = message.text.split()
        payment: types.ChatMember = await bot.get_chat_member(OWNER, OWNER)

        if z[0] == '+' or z[0] == '-' and len(z) == 1:
            await state.update_data(zvit = z[0])

            data = await state.get_data()

            if message.from_user.id != OWNER:
                cursor.execute(
                    f'INSERT INTO public.order_info_programming(id_order, id_customer, name_object, number_lab, variant_lab, tasks, zvit) VALUES ('f'{data["order_id"]}, {data["customer_id"]}, \'{data["select_object"]}\', \'{data["number_lab"]}\', {data["variant_lab"]}, \'{data["task"]}\', \'{data["zvit"]}\');')
                conn.commit()

            number_lab = data['number_lab']
            zvit = data['zvit']
            task = data['task']

            await message.reply('Дякуємо за замовлення. Скоро звами зв\'яжуться наші менеджери',
                                reply_markup=start_menu())

            await message.answer(
                'Ваш чек.\n\n'
                f'ID заказа: {data["order_id"]}\n' \
                f'ID замовника: {data["customer_id"]}\n' \
                f'Username: {message.from_user.username}\n' \
                f'First Name: {message.from_user.first_name}\n' \
                f'Last Name: {message.from_user.last_name}\n' \
                f'Предмет: {data["select_object"]}\n' \
                f'Номер лабораторної: {data["number_lab"]}\n' \
                f'З звітами: {data["zvit"]}\n' \
                f'Варіант Лабораторної: {data["variant_lab"]}\n' \
                f'Завдання: {data["task"]}\n\n' \
                f'Ціна: {price[0][f"{number_lab}"][f"{zvit}"][f"{task}"]} грн.\n' \
                'Час виконання: 1-2 дня\n' \
                f'Щоб оплатити зверніться до {payment.user.mention}'
            )

            await bot.send_message(
                CHAT,
                f'ID заказа: {data["order_id"]}\n' \
                f'ID замовника: {data["customer_id"]}\n' \
                f'Username: {message.from_user.username}\n' \
                f'First Name: {message.from_user.first_name}\n' \
                f'Last Name: {message.from_user.last_name}\n' \
                f'Предмет: {data["select_object"]}\n' \
                f'Номер лабораторної: {data["number_lab"]}\n' \
                f'З звітами: {data["zvit"]}\n' \
                f'Варіант Лабораторної: {data["variant_lab"]}\n' \
                f'Завдання: {data["task"]}\n\n' \
                f'Ціна: {price[0][f"{number_lab}"][f"{zvit}"][f"{task}"]} грн.\n'
            )

            await state.reset_state(with_data=True)

        else:
            await message.reply('Неправильний ввод. Будь ласка вкажіть правильно!')

    except Exception as e:
        logging.exception(e)
    finally:
        if conn:
            cursor.close()
            conn.close()

def register_handlers_programming(dp: Dispatcher):
    try:
        dp.register_message_handler(start_order, Text(equals = '💸 Зробити замовлення'), state = None)
        dp.register_message_handler(cancel_order, state = "*", commands = ['back'])
        dp.register_message_handler(cancel_order, Text(equals = 'Отмена'), state = "*")
        dp.register_message_handler(input_subject, Text(equals = 'Програмування'), state = Order.waiting_subject)
        dp.register_message_handler(input_number_lab, state = Order.waiting_number_lab)
        dp.register_message_handler(input_lab_variant, state = Order.waiting_variant)
        dp.register_message_handler(input_task, state = Order.waiting_zvit)
        dp.register_message_handler(input_zvit, state = Order.waiting_count_task)
    except Exception as e:
        logging.exception(e)