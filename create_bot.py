import aiogram

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TOKEN

storage = MemoryStorage()

bot = Bot(TOKEN, parse_mode = types.ParseMode.HTML)
dp = Dispatcher(bot, storage = storage)