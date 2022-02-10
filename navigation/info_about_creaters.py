import aiogram
import logging

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text

from config import OWNER, SECOND_MAN
from create_bot import bot

#@dp.message_handler(Text(equals = 'Інформація'))
async def informations(message: types.Message):
    try:
        man1: types.ChatMember = await bot.get_chat_member(OWNER, OWNER)
        man2: types.ChatMember = await bot.get_chat_member(SECOND_MAN, SECOND_MAN)

        await message.answer(
            'Привіт ми раді, що ви користуєтеся нашим ботом. 🥰\n'\
            'Цього бота й ідею розробили двоє студентів, яким завжди не хватало на каву ^^\n\n'\
            f'Розобник бота - Holo4ka.\n'\
            f'Допоміг з розвитком ідеї - Fisvif.\n\n'\
            f'Якщо у вас виникли проблеми з ботом пишіть сюда {man1.user.username}'
        )

    except Exception as e:
        logging.exception(e)

def register_handlers_informations(dp: Dispatcher):
    try:
        dp.register_message_handler(informations, Text(equals = 'ℹ️ Інформація'))
    except Exception as e:
        logging.exception(e)