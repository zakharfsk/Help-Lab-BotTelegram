import aiogram
import logging

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from create_bot import dp
from create_keyboards.keyboards import idz_hight_math_keyboard
from config import idz_hight_math_buttons


async def idz_1(message: types.Message):
    try:
        await message.answer(
            'Хей. А ось і прайс лист для Вашого ІДЗ №1, будем раді вашому замовлені ^^\n\n' \
            '<code>150 грн</code>',
            reply_markup = idz_hight_math_keyboard().add('Назад в меню')
        )
    except Exception as e:
        logging.exception(e)

async def idz_2(message: types.Message):
    try:
        await message.answer(
            'Хей. А ось і прайс лист для Вашого ІДЗ №2, будем раді вашому замовлені ^^\n\n' \
            '<code>150 грн</code>',
            reply_markup = idz_hight_math_keyboard().add('Назад в меню')
        )
    except Exception as e:
        logging.exception(e)

async def idz_3(message: types.Message):
    try:
        await message.answer(
            'Хей. А ось і прайс лист для Вашого ІДЗ №3, будем раді вашому замовлені ^^\n\n' \
            '<code>200 грн</code>',
            reply_markup = idz_hight_math_keyboard().add('Назад в меню')
        )
    except Exception as e:
        logging.exception(e)

async def idz_4(message: types.Message):
    try:
        await message.answer(
            'Хей. А ось і прайс лист для Вашого ІДЗ №4, будем раді вашому замовлені ^^\n\n' \
            '<code>300 грн</code>',
            reply_markup = idz_hight_math_keyboard().add('Назад в меню')
        )
    except Exception as e:
        logging.exception(e)


async def idz_5(message: types.Message):
    try:
        await message.answer(
            'Хей. А ось і прайс лист для Вашого ІДЗ №5, будем раді вашому замовлені ^^\n\n' \
            '<code>300 грн</code>',
            reply_markup = idz_hight_math_keyboard().add('Назад в меню')
        )
    except Exception as e:
        logging.exception(e)

def register_handlers_price_hight_math(dp: Dispatcher):
    try:
        dp.register_message_handler(idz_1, Text(equals = idz_hight_math_buttons[0]))
        dp.register_message_handler(idz_2, Text(equals = idz_hight_math_buttons[1]))
        dp.register_message_handler(idz_3, Text(equals = idz_hight_math_buttons[2]))
        dp.register_message_handler(idz_4, Text(equals = idz_hight_math_buttons[3]))
        dp.register_message_handler(idz_5, Text(equals = idz_hight_math_buttons[4]))
    except Exception as e:
        logging.exception(e)