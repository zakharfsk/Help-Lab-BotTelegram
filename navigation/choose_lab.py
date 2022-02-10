import aiogram
import logging

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text

from create_keyboards.keyboards import *

async def lab_for_prog(message: types.Message):
    try:
        await message.answer(
            'Яку лабораторну роботу бажає мій шановний пан, щоб я за нього її виконала. 😘',
            reply_markup = labaratories_keyboard().add('Назад в меню')
        )

    except Exception as e:
        logging.exception(e)


async def lab_for_it(message: types.Message):
    try:
        await message.answer(
            'Яку лабораторну роботу бажає мій шановний пан, щоб я за нього її виконала. 😘',
            reply_markup = it_keyboard().add('Назад в меню')
        )

    except Exception as e:
        logging.exception(e)

async def idz_hight_math(message: types.Message):
    try:
        await message.answer(
            'Яку лабораторну роботу бажає мій шановний пан, щоб я за нього її виконала. 😘',
            reply_markup = idz_hight_math_keyboard().add('Назад в меню')
        )
    except Exception as e:
        logging.exception(e)

async def web_tehnology(message: types.Message):
    try:
        await message.answer(
            'Яку лабораторну роботу бажає мій шановний пан, щоб я за нього її виконала. 😘',
            reply_markup = web_buttons().add('Назад в меню')
        )
    except Exception as e:
        logging.exception(e)

def register_handlers_choose_lab(dp: Dispatcher):
    try:
        dp.register_message_handler(lab_for_prog, Text(equals = 'Лабораторні з програмування'))
        dp.register_message_handler(lab_for_it, Text(equals = 'Лабораторні з інформаціїних технологій'))
        dp.register_message_handler(idz_hight_math, Text(equals = 'Вища математика'))
        dp.register_message_handler(web_tehnology, Text(equals='Web Технології'))
    except Exception as e:
        logging.exception(e)