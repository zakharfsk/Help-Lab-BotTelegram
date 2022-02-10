import logging

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text, Command
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from config import CHAT, start_buttons
from create_bot import bot
from create_keyboards.keyboards import start_menu

class FeedbackState(StatesGroup):
    take_feedback = State()

async def takes_feedback(message: types.Message, state: FSMContext):
    try:
        await FeedbackState.take_feedback.set()
        await message.reply(
            'Ведіть ваш текст. 🙂',
            reply_markup = types.ReplyKeyboardMarkup(resize_keyboard = True).add('Отмена')
        )
    except Exception as e:
        logging.exception(e)

async def cancel_send_feedback(message: types.Message, state: FSMContext):
    try:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.reset_state(with_data = True)

        await message.reply(
            'Ну ок. 😔',
            reply_markup = start_menu()
        )

    except Exception as e:
        logging.exception(e)

async def send_feedback(message: types.Message, state: FSMContext):
    try:
        text = message.text
        # telephone = message.contact.phone_number

        await bot.send_message(
            CHAT,
            f'Новий Feedback від користувача {message.from_user.first_name}\n'\
            f'ID: {message.from_user.id}\n'\
            f'Username: {message.from_user.username}\n\n'\
            f'Feedback: {text}'
        )

        await message.answer(
            'Чудово! Ваш feedback був відправлений.',
            reply_markup = start_menu()
        )
        await state.reset_state(with_data = True)

    except Exception as e:
        logging.exception(e)

def register_message_handler_feedback(dp: Dispatcher):
    dp.register_message_handler(takes_feedback,
                                Text(equals = start_buttons[5]),
                                state = None)
    dp.register_message_handler(cancel_send_feedback,
                                Text(equals = 'Отмена'),
                                state = "*")
    dp.register_message_handler(send_feedback, state = FeedbackState.take_feedback)
