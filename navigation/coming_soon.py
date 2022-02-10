import aiogram
import logging

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text

#@dp.message_handler(Text(equals = 'Coming soon...'))
async def coming_soon(message: types.Message):
    try:
        await message.answer('Хей. Скоро появляться й інши предмети з яких ти зможеш замовити готову домашку ^^')
    except Exception as e:
        logging.exception(e)

def register_handlers_coming_soon(dp: Dispatcher):
    try:
        dp.register_message_handler(coming_soon, Text(equals = 'Coming soon...'))
    except Exception as e:
        logging.exception(e)