import aiogram
import logging

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from create_bot import dp
from create_keyboards.keyboards import it_keyboard
from config import it_buttons

async def laboratories_it_numb1(message: types.Message):
    try:
        await message.answer(
            f'Хей. А ось і прайс лист для Вашої {it_buttons[0]}, будем раді вашому замовлені ^^\n\n'\
            '<code>-99.99 грн за лабораторну</code>',
            reply_markup = it_keyboard().add('Назад в меню')
        )
    except Exception as e:
        logging.exception(e)

async def laboratories_it_numb2(message: types.Message):
    try:
        await message.answer(
            f'Хей. А ось і прайс лист для Вашої {it_buttons[1]}, будем раді вашому замовлені ^^\n\n'\
            '<code>-99.99 грн за лабораторну</code>',
            reply_markup = it_keyboard().add('Назад в меню')
        )
    except Exception as e:
        logging.exception(e)

async def laboratories_it_numb3(message: types.Message):
    try:
        await message.answer(
            f'Хей. А ось і прайс лист для Вашої {it_buttons[2]}, будем раді вашому замовлені ^^\n\n'\
            '<code>-99.99 грн за лабораторну</code>',
            reply_markup = it_keyboard().add('Назад в меню')
        )
    except Exception as e:
        logging.exception(e)

async def laboratories_it_numb4(message: types.Message):
    try:
        await message.answer(
            f'Хей. А ось і прайс лист для Вашої {it_buttons[3]}, будем раді вашому замовлені ^^\n\n'\
            '<code>-350 грн за фотошоп.\n'\
            'Якщо без блок-схем - 300 грн</code>',
            reply_markup = it_keyboard().add('Назад в меню')
        )
    except Exception as e:
        logging.exception(e)

async def laboratories_it_numb5(message: types.Message):
    try:
        await message.answer(
            f'Хей. А ось і прайс лист для Вашої {it_buttons[4]}, будем раді вашому замовлені ^^\n\n'\
            '<code>149.99 грн за лабораторну.\n'\
            'Якщо ви хочете свою модельку - 499.99 грн</code>',
            reply_markup = it_keyboard().add('Назад в меню')
        )
    except Exception as e:
        logging.exception(e)

async def laboratories_it_numb6(message: types.Message):
    try:
        await message.answer(
            f'Хей. А ось і прайс лист для Вашої {it_buttons[5]}, будем раді вашому замовлені ^^\n\n'\
            '<code>124.99 грн за лабораторну.</code>',
            reply_markup = it_keyboard().add('Назад в меню')
        )
    except Exception as e:
        logging.exception(e)

async def laboratories_it_numb7(message: types.Message):
    try:
        await message.answer(
            f'Хей. А ось і прайс лист для Вашої {it_buttons[6]}, будем раді вашому замовлені ^^\n\n'\
            '<code>-Завдання на оцінку «3»: 149.99 грн\n'\
            '-Завдання на оцінку «4»: 199.99 грн\n'\
            '-Завдання на оцінку «5»: 249.99 грн</code>',
            reply_markup = it_keyboard().add('Назад в меню')
        )
    except Exception as e:
        logging.exception(e)

async def laboratories_it_numb8(message: types.Message):
    try:
        await message.answer(
            f'Хей. А ось і прайс лист для Вашої {it_buttons[7]}, будем раді вашому замовлені ^^\n\n'\
            '<code>200 грн за лабораторну.</code>',
            reply_markup = it_keyboard().add('Назад в меню')
        )
    except Exception as e:
        logging.exception(e)

def register_handlers_price_IT(dp: Dispatcher):
    try:
        dp.register_message_handler(laboratories_it_numb1, Text(equals = it_buttons[0]))
        dp.register_message_handler(laboratories_it_numb2, Text(equals = it_buttons[1]))
        dp.register_message_handler(laboratories_it_numb3, Text(equals = it_buttons[2]))
        dp.register_message_handler(laboratories_it_numb4, Text(equals = it_buttons[3]))
        dp.register_message_handler(laboratories_it_numb5, Text(equals = it_buttons[4]))
        dp.register_message_handler(laboratories_it_numb6, Text(equals = it_buttons[5]))
        dp.register_message_handler(laboratories_it_numb7, Text(equals = it_buttons[6]))
        dp.register_message_handler(laboratories_it_numb8, Text(equals = it_buttons[7]))
    except Exception as e:
        logging.exception(e)