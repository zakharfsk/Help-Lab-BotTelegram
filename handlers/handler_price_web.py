import aiogram
import logging

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from create_bot import dp
from config import web_buttons


async def web_lab(message: types.Message):
    try:
        pass
    except Exception as e:
        logging.exception(e)

async def web_pract(message: types.Message):
    try:
        pass
    except Exception as e:
        logging.exception(e)

def register_message_handler_web(dp: Dispatcher):
    dp.register_message_handler(
        web_lab,
        Text(equals = web_buttons[0])
    )

    dp.register_message_handler(
        web_lab,
        Text(equals = web_buttons[1])
    )