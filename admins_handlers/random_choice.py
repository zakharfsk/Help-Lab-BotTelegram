import logging

import aiogram
import random
import psycopg2
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.builtin import Command
from config import DATABASE, ENGLISH_MAN_1, ENGLISH_MAN_2, HOST, OWNER, PASSWORD, SECOND_MAN, USER
from create_bot import bot, dp

username = USER
host = HOST
database = DATABASE
password = PASSWORD
port = 5432

async def choice_winner(message: types.Message):
    try:
        conn = psycopg2.connect(
            user = username,
            host = host,
            database = database,
            password = password,
            port = port
        )

        cursor = conn.cursor()
    
        cursor.execute(f'SELECT id FROM public.user_info')
        users_ids = cursor.fetchall()

        winners = []
        awards = [
            'виграв 2 відповіді на його вибір',
            'виграв 2 відповіді на його вибір',
            'виграв скидку 25% на відповіді',
            'виграв скидку 25% на відповіді',
            'виграв скидку 25% на відповіді'
        ]

        for i in range(5):
            winners.append(random.choice(users_ids)[0])
        
        for i in range(len(winners)):

            winner: types.ChatMember = await bot.get_chat_member(winners[i], winners[i])
            
            if winner.user.id != OWNER and winner.user.id != SECOND_MAN and winner.user.id != ENGLISH_MAN_1 and winner.user.id != ENGLISH_MAN_2:
                await message.answer(f'{winner.user.mention} {awards[i]}')

    except Exception as e:
        logging.exception(e)

    finally:
        if conn:
            cursor.close()
            conn.close()

def register_handlers_choice_winner(dp: Dispatcher):
    try:
        dp.register_message_handler(
            choice_winner,
            Command('choice_winner'),
            lambda message: OWNER == message.from_user.id or SECOND_MAN == message.from_user.id
        )
    except Exception as e:
        logging.exception(e)
