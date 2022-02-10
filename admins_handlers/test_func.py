import aiogram
import logging

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.utils.exceptions import BotBlocked

from config import OWNER
from create_bot import bot, dp

async def test_func(message: types.Message):
    try:
        pass
    except Exception as e:
        logging.exception(e)

def register_handlers_test(dp: Dispatcher):
    try:
        dp.register_message_handler(test_func, Command('test'), lambda message: OWNER == message.from_user.id)
    except Exception as e:
        logging.exception(e)