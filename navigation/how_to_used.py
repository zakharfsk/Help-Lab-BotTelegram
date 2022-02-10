import aiogram
import logging

from aiogram.dispatcher.filters import Text
from aiogram import types, Dispatcher

from create_bot import bot
from create_keyboards.keyboards import instruction_keyboard

phrases_price = [
    '1. Щоб подивитися прайс до Лабораторних робіт з предметів нажміть в головному меню <b>Подивитися прайс</b>.',
    '2. Далі потрібно вибрати предмет.',
    '3. Після того як Ви вибрали предмет вам буде доступний вибір лабораторних по цьому предметі.',
    '4. Вибравши номер лабораторної, вам буде надіслано повідомлення з інформацією про цю лабораторну, де буде вказана ціна.'
]

phrases_order = [
    '1. Щоб почати заповнювати анкету, в головному меню нажміть <b>Зробити замовлення</b>.',
    '2. Далі з списка виберіть предмет.',
    '3. Після цього оберіть номер лабораторної.',
    '4. Вкажіть носмер вашого варіанта. Варіант має бути числом, текс не приймаємо )',
    '5. Далі вам потрібно вказати кількість завдань.\n\n'\
    'Де їх взяти і як правильно вказати?\n'\
    'Їх взяти можна в прайсі до лабораторних( як подивитися прайс інструкція є )\n\n'\
    'Наприлкад, ми заказуємо Лабораторну №1, тоді треба буде написати: кількість завдань з лабораторноїі, '\
    'номери завдань і з звітом чи без, приклад на фото( аналогічно заповнюються анкети до інших лабораторних).',
    '6. Після чого ви отримаєте свій чек.'
]

async def how_to_used_bot(message: types.Message):
    try:
        await message.answer(
            'Яка саме інструкція вас цікавить?',
            reply_markup = instruction_keyboard().add('Назад в меню')
        )

    except Exception as e:
        logging.exception(e)

async def prices(message: types.Message):
    try:

        for i in range(len(phrases_price)):
            await bot.send_photo(
                message.from_user.id,
                open(f'data/photo/price/price{i}.png', 'rb'),
                caption = f'{phrases_price[i]}'
            )

    except Exception as e:
        logging.exception(e)

async def how_correctly_take_order(message: types.Message):
    try:

        for i in range(len(phrases_order)):
            await bot.send_photo(
                message.from_user.id,
                open(f'data/photo/order/order{i}.png', 'rb'),
                caption = f'{phrases_order[i]}'
            )

    except Exception as e:
        logging.exception(e)

async def payments(message: types.Message):
    try:
        await bot.send_photo(
            message.from_user.id,
            open('data/photo/payments/paymants.png', 'rb'),
            caption = 'В чекові вказана людина до якої зверататия за оплатою.\n'\
            'Оплатити можна на карточку або налом.\n\n'\
            'Виконання завдання начинається лише після оплати'
        )
    except Exception as e:
        logging.exception(e)

def register_handler_how_to_used_bot(dp: Dispatcher):
    try:
        dp.register_message_handler(how_to_used_bot, Text(equals = '📝 Інструкція використання'))
        dp.register_message_handler(prices, Text(equals = 'Ціни'))
        dp.register_message_handler(how_correctly_take_order, Text(equals = 'Як оформити правильно заказ?'))
        dp.register_message_handler(payments, Text(equals = 'Оплата'))
    except Exception as e:
        logging.exception(e)
