import aiogram
import uuid
import logging
import psycopg2

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from create_bot import dp, bot
from config import USER, HOST, DATABASE, PASSWORD, OWNER, CHAT, \
    select_object_buttons
from create_keyboards.keyboards import subject_keyboard, start_menu, cancel_keyboard,\
    idz_hight_math_keyboard, idz_hight_math_buttons

username = USER
host = HOST
database = DATABASE
password = PASSWORD
port = 5432

class Order(StatesGroup):
    waiting_subject = State()
    waiting_number_idz = State()
    waiting_variant_idz = State()
    waiting_pack_idz = State()

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
            await message.reply('Виберіть ІДЗ.', reply_markup = idz_hight_math_keyboard().add('Отмена'))
        else:
            await message.reply(
                'Упсс...\n'\
                'Нажаль такого предмета немає'
            )
    except Exception as e:
        logging.exception(e)

async def input_number_group(message: types.Message, state: FSMContext):
    try:
        num_idz = message.text
        if num_idz in idz_hight_math_buttons:
            await state.update_data(number_idz = num_idz)
            await message.reply('Вкажіть вашу групу.(в форматі КІ-21-2)', reply_markup = cancel_keyboard())
            await Order.next()
        else:
            await message.reply(
                'Упс...\n'
                'Нажаль в нас немає такого ІДЗ'
            )
    except Exception as e:
        logging.exception(e)

async def input_number_in_list(message: types.Message, state: FSMContext):
    try:
        number_group = message.text

        await state.update_data(number_group = number_group)
        await Order.next()
        await message.reply(
            'Вкажіть номер під яким ви в списку групи.',
            reply_markup = cancel_keyboard()
        )

    except Exception as e:
        logging.exception(e)

async def input_pack_type(message: types.Message, state: FSMContext):
    try:

        conn = psycopg2.connect(
            user = username,
            host = host,
            database = database,
            password = password,
            port = port
        )

        cursor = conn.cursor()

        number_in_list = message.text
        payment: types.ChatMember = await bot.get_chat_member(OWNER, OWNER)

        await state.update_data(number_in_list = number_in_list)
        data = await state.get_data()

        if message.from_user.id != OWNER:
            cursor.execute(f'INSERT INTO public.order_info_hight_math(id_order, id_customer, name_object, number_idz, user_group, number_in_list) VALUES ('f'{data["order_id"]}, {data["customer_id"]}, \'{data["select_object"]}\', \'{data["number_idz"]}\', \'{data["number_group"]}\', \'{data["number_in_list"]}\');')
            conn.commit()

        await message.reply('Дякуємо за замовлення. Скоро звами зв\'яжуться наші менеджери', reply_markup = start_menu())

        await message.answer(
            'Ваш чек.\n\n'
            f'ID заказа: {data["order_id"]}\n' \
            f'ID замовника: {data["customer_id"]}\n' \
            f'Username: {message.from_user.username}\n' \
            f'First Name: {message.from_user.first_name}\n' \
            f'Last Name: {message.from_user.last_name}\n' \
            f'Предмет: {data["select_object"]}\n' \
            f'Номер ІДЗ: {data["number_idz"]}\n' \
            f'Група: {data["number_group"]}\n' \
            f'Номер в списку: {data["number_in_list"]}\n\n'\
            'Час виконання: 1-2 дня\n'\
            f'Щоб оплатити зверніться до {payment.user.mention}'
        )

        await bot.send_message(
            CHAT,
            f'ID заказа: {data["order_id"]}\n'\
            f'ID замовника: {data["customer_id"]}\n'\
            f'Username: {message.from_user.username}\n'\
            f'First Name: {message.from_user.first_name}\n'\
            f'Last Name: {message.from_user.last_name}\n'\
            f'Предмет: {data["select_object"]}\n'\
            f'Номер ІДЗ: {data["number_idz"]}\n'\
            f'Група: {data["number_group"]}\n'\
            f'Номер в списку: {data["number_in_list"]}\n'\
        )

        await state.reset_state(with_data = True)

    except Exception as e:
        logging.exception(e)
    finally:
        if conn:
            cursor.close()
            conn.close()

def register_handlers_math(dp: Dispatcher):
    try:
        dp.register_message_handler(start_order, Text(equals = '💸 Зробити замовлення'), state = None)
        dp.register_message_handler(cancel_order, state = "*", commands = ['back'])
        dp.register_message_handler(cancel_order, Text(equals = 'Отмена'), state = "*")
        dp.register_message_handler(input_subject, Text(equals = 'Вища математика'), state = Order.waiting_subject)
        dp.register_message_handler(input_number_group, state = Order.waiting_number_idz)
        dp.register_message_handler(input_number_in_list, state = Order.waiting_variant_idz)
        dp.register_message_handler(input_pack_type, state = Order.waiting_pack_idz)
    except Exception as e:
        logging.exception(e)