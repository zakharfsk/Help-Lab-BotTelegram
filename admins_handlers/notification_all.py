import asyncio

import aiogram
import logging
import psycopg2

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command, Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.exceptions import BotBlocked

from config import OWNER, SECOND_MAN, CHAT, HOST, PASSWORD, USER, DATABASE
from create_bot import bot, dp
from create_keyboards.keyboards import start_menu

username = USER
host = HOST
database = DATABASE
password = PASSWORD
port = 5432


class SendMessageAllUsers(StatesGroup):
    start_sendings = State()


async def input_text_for_message(message: types.Message, state: FSMContext):
    try:
        await SendMessageAllUsers.start_sendings.set()
        await message.reply(
            'Ведіть текст для розсилки',
            reply_markup = types.ReplyKeyboardMarkup(resize_keyboard = True).add('Отмена розсилки')
        )
    except Exception as e:
        logging.exception(e)


async def cancel_send_message_all_users(message: types.Message, state: FSMContext):
    try:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.reset_state(with_data = True)

        await message.reply(
            'Розсилка зупинена',
            reply_markup = start_menu()
        )

    except Exception as e:
        logging.exception(e)


async def send_text_all_users(message: types.Message, state: FSMContext):
    try:
        message_for_sending = message.text
        

        conn = psycopg2.connect(
            user = username,
            host = host,
            database = database,
            password = password,
            port = port
        )

        cursor = conn.cursor()

        cursor.execute(f'SELECT id FROM public.user_info')
        users_ids = cursor.fetchall()

        await message.answer(
            'Розсилка почалась. Очікуйте повідомлення про її закінчення.',
            reply_markup = start_menu()
        )

        await message.answer(message)
        

        for i in range(len(users_ids)):
            try:
                
                await bot.send_message(
                    users_ids[i][0],
                    f'{message_for_sending}'
                )
#                 await dp.bot.send_video(
#                     users_ids[i][0],
#                     open(r'data/video/winners.mp4', 'rb'),
#                     caption = '''
# А вот і наші переможці:

# @nazzzzzzzarrr - виграв 2 відповіді на його вибір
# Дімас - виграв 2 відповіді на його вибір
# @jkeejj - виграв скидку 25% на відповіді
# Maksim Zaveryuha - виграв скидку 25% на відповіді
# @Myykytaa - виграв скидку 25% на відповіді

# Протягом 2-х годин зв'яжіться з адміністраторами для отримання приза.
# Якщо протягом цього періоду переможець не зв'яжется то його буде перевибрано.

# Дякуємо всім за участь
# '''
#                 )

                await asyncio.sleep(1.5)
            except BotBlocked:
                cursor.execute(f'DELETE FROM public.user_info WHERE id = {users_ids[i][0]}')
                conn.commit()
                await message.answer(f'Видалено: {users_ids[i][0]}')

        info_about_sending = await bot.send_message(
            CHAT,
            f'Повідомлення було надіслане {len(users_ids)} користувачам бота\n\n' \
            f'Текст повідомлення:\n{message_for_sending}',
        )

        await bot.pin_chat_message(
            CHAT,
            info_about_sending.message_id,
            disable_notification = False
        )

        await state.reset_state(with_data = True)

    except Exception as e:
        logging.exception(e)


def register_handlers_rozsilaca_messages(dp: Dispatcher):
    try:
        dp.register_message_handler(input_text_for_message, Command('rozsilca'),
                                    lambda message: OWNER == message.from_user.id or SECOND_MAN == message.from_user.id)
        dp.register_message_handler(cancel_send_message_all_users,
                                    Text(equals = 'Отмена розсилки'),
                                    state = "*")
        dp.register_message_handler(send_text_all_users,
                                    state = SendMessageAllUsers.start_sendings)
    except Exception as e:
        logging.exception(e)