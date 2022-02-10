import aiogram
import logging

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text

from create_keyboards.keyboards import start_menu

#@dp.message_handler(Text(equals = 'Назад в меню'))
async def back_to_menu(message: types.Message):
    try:
        await message.answer(
            'Ти в головному меню.',
            reply_markup = start_menu()
        )

    except Exception as e:
        logging.exception(e)

def register_handlers_back_to_menu(dp: Dispatcher):
    try:
        dp.register_message_handler(back_to_menu, Text(equals = 'Назад в меню'))
    except Exception as e:
        logging.exception(e)