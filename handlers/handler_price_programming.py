import aiogram
import logging

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from create_bot import dp
from create_keyboards.keyboards import labaratories_keyboard
from config import labaratories_buttons

async def laboratories_numb1(message: types.Message):
    try:
        await message.answer(
            'Хей. А ось і прайс лист для Вашої Лабораторної роботи №1, будем раді вашому замовлені ^^\n\n'\
            '<code>4 завдань по 94.99 грн + звіти 40 грн -  25% скидка\n'\
            '3 завдань по 79.99 грн + звіти 30 грн -  15% скидка\n'\
            '2 завдання по 54.99 грн + звіти 20 грн  - 10% скидка\n'\
            '1 завдання 30 грн  + 15 грн звіт</code>\n\n'\
            '*Всі ціни вже вказані з врахуванням вказаної знижки.',
            reply_markup = labaratories_keyboard().add('Назад в меню')
        )

    except Exception as e:
        logging.exception(e)

async def laboratories_numb2(message: types.Message):
    try:
        await message.answer(
            'Хей. А ось і прайс лист для Вашої Лабораторної роботи №2, будем раді вашому замовлені ^^\n\n'\
            '<code>6 завдань по 139.99 грн + звіти 75 грн -  25% скидка\n'\
            '5 завдань по 114.99 грн + звіти 65 грн -  25% скидка\n'\
            '4 завдання по 109.99 грн + звіти 55 грн  - 10% скидка\n'\
            '3 завдання по 79.99 грн + звіти 45 грн  - 10% скидка\n'\
            '2 завдання по 54.99 грн + звіти 35 грн  - 10% скидка\n'\
            '1 завдання 29.99 грн  + 30 грн звіт</code>\n\n'\
            '*Всі ціни вже вказані з врахуванням вказаної знижки.',
            reply_markup = labaratories_keyboard().add('Назад в меню')
        )

    except Exception as e:
        logging.exception(e)

async def laboratories_numb3(message: types.Message):
    try:
        await message.answer(
            'Хей. А ось і прайс лист для Вашої Лабораторної роботи №2, будем раді вашому замовлені ^^\n\n'\
            '<code>6 завдань по 139.99 грн + звіти 75 грн -  25% скидка\n'\
            '5 завдань по 114.99 грн + звіти 65 грн -  25% скидка\n'\
            '4 завдання по 109.99 грн + звіти 55 грн  - 10% скидка\n'\
            '3 завдання по 79.99 грн + звіти 45 грн  - 10% скидка\n'\
            '2 завдання по 54.99 грн + звіти 35 грн  - 10% скидка\n'\
            '1 завдання 29.99 грн  + 30 грн звіт</code>\n\n'\
            '*Всі ціни вже вказані з врахуванням вказаної знижки.',
            reply_markup = labaratories_keyboard().add('Назад в меню')
        )

    except Exception as e:
        logging.exception(e)

async def laboratories_numb4(message: types.Message):
    try:
        await message.answer(
            'Хей. А ось і прайс лист для Вашої Лабораторної роботи №4, будем раді вашому замовлені ^^\n\n'\
            '<code>3 завдань по 69.99 грн + звіти 45 грн -  25% скидка\n'\
            '2 завдання по 54.99 грн + звіти 35 грн  - 10% скидка\n'\
            '1 завдання 29.99 грн  + 30 грн звіт</code>\n\n'\
            '*Всі ціни вже вказані з врахуванням вказаної знижки.\n',
            reply_markup = labaratories_keyboard().add('Назад в меню')
        )

    except Exception as e:
        logging.exception(e)

async def laboratories_numb5(message: types.Message):
    try:
        await message.answer(
            'Хей. А ось і прайс лист для Вашої Лабораторної роботи №5, будем раді вашому замовлені ^^\n\n'\
            '<code>4 завдань по 104.99 грн + звіти 55 грн -  25% скидка\n'\
            '3 завдань по 89.99 грн + звіти 45 грн -  15% скидка\n'\
            '2 завдання по 64.99 грн + звіти 35 грн - 10% скидка\n'\
            '1 завдання 34.99 грн  + 30 грн звіт </code>\n\n'\
            '*Всі ціни вже вказані з врахуванням вказаної знижки.',
            reply_markup = labaratories_keyboard().add('Назад в меню')
        )

    except Exception as e:
        logging.exception(e)

async def laboratories_numb6(message: types.Message):
    try:
        await message.answer(
            'Хей. А ось і прайс лист для Вашої Лабораторної роботи №6, будем раді вашому замовлені ^^\n\n'\
            '<code>6 завдань по 154.99 грн + звіти 75 грн-  25% скидка\n'\
            '5 завдань 129.99 грн + звіти 65 грн -  25% скидка\n'\
            '4 завдань 124.99 грн + звіти 55 - 10% скидка\n'\
            '3 завдань 94.99 грн + звіти 45 - 10% скидка\n'\
            '2 завдань 64.99 грн + звіти 35 - 10% скидка\n'\
            '1 завдання 33.99 грн  + 30 грн звіт</code>\n\n'\
            '*Всі ціни вже вказані з врахуванням вказаної знижки.',
            reply_markup = labaratories_keyboard().add('Назад в меню')
        )

    except Exception as e:
        logging.exception(e)

async def laboratories_numb7(message: types.Message):
    try:
        await message.answer(
            'Хей. А ось і прайс лист для Вашої Лабораторної роботи №7, будем раді вашому замовлені ^^\n\n'\
            '<code>2 завдання по 54.99 грн + звіти 35грн - 15% скидка\n'\
            '1 завдання 29.99 грн  + 30 грн звіт</code>\n\n'\
            '*Всі ціни вже вказані з врахуванням вказаної знижки.',
            reply_markup = labaratories_keyboard().add('Назад в меню')
        )

    except Exception as e:
        logging.exception(e)

async def laboratories_numb8(message: types.Message):
    try:
        await message.answer(
            'Хей. А ось і прайс лист для Вашої Лабораторної роботи №8, будем раді вашому замовлені ^^\n\n'\
            '<code>2 завдання по 109.99 грн + звіти 35 грн - 15% скидка\n'\
            '1 завдання 59.99 грн  + 30 грн звіт</code>\n\n'\
            '*Всі ціни вже вказані з врахуванням вказаної знижки.',
            reply_markup = labaratories_keyboard().add('Назад в меню')
        )

    except Exception as e:
        logging.exception(e)

def register_handlers_price_programming(dp: Dispatcher):
    try:
        dp.register_message_handler(laboratories_numb1, Text(equals = labaratories_buttons[0]))
        dp.register_message_handler(laboratories_numb2, Text(equals = labaratories_buttons[1]))
        dp.register_message_handler(laboratories_numb3, Text(equals = labaratories_buttons[2]))
        dp.register_message_handler(laboratories_numb4, Text(equals = labaratories_buttons[3]))
        dp.register_message_handler(laboratories_numb5, Text(equals = labaratories_buttons[4]))
        dp.register_message_handler(laboratories_numb6, Text(equals = labaratories_buttons[5]))
        dp.register_message_handler(laboratories_numb7, Text(equals = labaratories_buttons[6]))
        dp.register_message_handler(laboratories_numb8, Text(equals = labaratories_buttons[7]))
    except Exception as e:
        logging.exception(e)