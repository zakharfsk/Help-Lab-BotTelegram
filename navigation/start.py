import aiogram
import psycopg2
import logging

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command

from create_bot import bot
from config import OWNER, USER, HOST, DATABASE, PASSWORD
from create_keyboards.keyboards import start_menu

username = USER
host = HOST
database = DATABASE
password = PASSWORD
port = 5432


async def _start_command(message: types.Message, state: FSMContext):
    try:
        conn = psycopg2.connect(
            user = username,
            host = host,
            database = database,
            password = password,
            port = port
        )

        cursor = conn.cursor()

        cursor.execute(f'SELECT id FROM user_info WHERE id = {message.from_user.id};')
        user_id = cursor.fetchone()

        if user_id is None and message.from_user.is_bot is False:
            cursor.execute(f'INSERT INTO public.user_info(id, username, first_name, last_name) VALUES ({message.from_user.id}, \'{message.from_user.username}\', \'{message.from_user.first_name}\', \'{message.from_user.last_name}\');')
            conn.commit()
            await bot.send_message(
                OWNER,
                'Новий користувач бота\n' \
                f'ID: {message.from_user.id}\n' \
                f'Username: {message.from_user.username}\n'\
                f'First Name: {message.from_user.first_name}\n'\
                f'Last Name: {message.from_user.last_name}'
            )
        conn.commit()

        await message.answer(
            'Привіт!\n'\
            'З допомогою цього бота ти замовиш Лабораторні роботи. 🥰🥰🥰\n\n'\
            'Як правильно оформлювати закази можна подивитися в головному меню, нажавши на кнопку <b>Інструкція використання</b>\n'\
            'Якщо заказ буде оформлений не по шаблону, він розглядатися не буде. Дякуємо за розуміння! 😊😊😊',
            reply_markup = start_menu()
        )
        await state.reset_state(with_data = True)
    except Exception as e:
        logging.exception(e)
    finally:
        if conn:
            cursor.close()
            conn.close()


def register_handlers_start_command(dp: Dispatcher):
    try:
        dp.register_message_handler(_start_command, Command('start'), state = "*")
    except Exception as e:
        logging.exception(e)