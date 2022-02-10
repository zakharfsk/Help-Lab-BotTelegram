import aiogram
import logging

from aiogram import types

from config import *

def subject_keyboard(type):
    try:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
        keyboard.add(*type)

        return keyboard

    except Exception as e:
        logging.exception(e)

def labaratories_keyboard():
    try:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
        keyboard.add(*labaratories_buttons)

        return keyboard

    except Exception as e:
        logging.exception(e)

def cancel_keyboard():
    try:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
        keyboard.add('Отмена')

        return keyboard

    except Exception as e:
        logging.exception(e)

def start_menu():
    try:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
        keyboard.add(*start_buttons)

        return keyboard

    except Exception as e:
        logging.exception(e)

def instruction_keyboard():
    try:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
        keyboard.add(*instruction_buttons)

        return keyboard

    except Exception as e:
        logging.exception(e)

def it_keyboard():
    try:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
        keyboard.add(*it_buttons)

        return keyboard
    except Exception as e:
        logging.exception(e)

def web_keyboard():
    try:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
        keyboard.add(*web_buttons)

        return keyboard
    except Exception as e:
        logging.exception(e)

def idz_hight_math_keyboard():
    try:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
        keyboard.add(*idz_hight_math_buttons)

        return keyboard
    except Exception as e:
        logging.exception(e)