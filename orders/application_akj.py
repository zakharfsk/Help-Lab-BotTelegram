import logging

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from create_bot import bot
from config import start_buttons, CHAT
from create_keyboards.keyboards import subject_keyboard, start_menu


async def get_applications(message: types.Message):
    try:
        await message.answer(
            'Дякуємо за залишену заявку!'\
            'Завтра з вами зв\'яжуться для отримання подальшої інформації.', 
        )

        await bot.send_message(
            CHAT,
            'Нова за\'явка на ГКР.\n'\
            f'ID замовника: {message.from_user.id}\n'\
            f'Username: {message.from_user.username}\n'\
            f'First Name: {message.from_user.first_name}\n'\
            f'Last Name: {message.from_user.last_name}\n'\
        )

    except Exception as e:
        logging.exception(e)

def register_message_handler_get_applications(dp: Dispatcher):
    try:
        dp.register_message_handler(get_applications, Text(equals = start_buttons[4]), state = "*")
    except Exception as e:
        logging.exception(e)