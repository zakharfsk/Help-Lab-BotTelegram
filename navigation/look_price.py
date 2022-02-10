import aiogram
import logging

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text

from create_keyboards.keyboards import subject_keyboard
from config import subject_buttons

#@dp.message_handler(Text(equals = 'Подивитися прайс'))
async def see_price(message: types.Message):
    try:
        await message.answer(
            'Вибири нище потрібний предмет ⬇',
            reply_markup = subject_keyboard(subject_buttons).add('Назад в меню')
        )

    except Exception as e:
        logging.exception(e)

def register_handlers_see_price(dp: Dispatcher):
    try:
        dp.register_message_handler(see_price, Text(equals = '👨‍🏫 Подивитися прайс'))
    except Exception as e:
        logging.exception(e)