import logging

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from config import subject_buttons, ENGLISH_MAN_1, ENGLISH_MAN_2
from create_bot import bot


async def tasks_english(message: types.Message):
    try:
        man1: types.ChatMember = await bot.get_chat_member(ENGLISH_MAN_1, ENGLISH_MAN_1)
        man2: types.ChatMember = await bot.get_chat_member(ENGLISH_MAN_2, ENGLISH_MAN_2)

        await message.answer(
            'Привіт!👋 Ми пока що не зійшлись на одній конкретній ціні, '\
            f'тому після того як ви заказали зв\'яжіться з {man1.user.mention} або {man2.user.mention}, щоб оговорити ціну. Дякуємо! 😊',
            reply_markup = types.ReplyKeyboardMarkup(resize_keyboard = True).add('Назад в меню')
        )
    except Exception as e:
        logging.exception(e)


def register_message_handler_english(dp: Dispatcher):
    try:
        dp.register_message_handler(tasks_english, Text(equals = subject_buttons[3]))
    except Exception as e:
        logging.exception(e)