import os

OWNER = 618042376  # Zakhar
SECOND_MAN = 876045214  # Vadim
CHAT = -1001714594820  # General Chat
ENGLISH_MAN_1 = 529254398  # Ira
ENGLISH_MAN_2 = 773978943  # Sasha

TOKEN = os.environ.get('TOKEN')
USER = os.environ.get('USER')
HOST = os.environ.get('HOST')
DATABASE = os.environ.get('DATABASE')
PASSWORD = os.environ.get('PASSWORD')

start_buttons = [
    '👨‍🏫 Подивитися прайс',
    '💸 Зробити замовлення',
    'ℹ️ Інформація',
    '📝 Інструкція використання',
    '📩 Залишити заявку на ГКР',
    '📤 Feedback'
]

subject_buttons = [
    'Лабораторні з програмування',
    'Вища математика',
    'Лабораторні з інформаціїних технологій',
    'Англійська мова',
    'Web Технології',
    'Coming soon...'
]

select_object_buttons = [
    'Програмування', 'Вища математика', 'Інформаціїні технології', 'Англійська мова'
]

labaratories_buttons = [
    'Лабораторна №1 з Програмування', 'Лабораторна №2 з Програмування',
    'Лабораторна №3 з Програмування', 'Лабораторна №4 з Програмування',
    'Лабораторна №5 з Програмування', 'Лабораторна №6 з Програмування',
    'Лабораторна №7 з Програмування', 'Лабораторна №8 з Програмування',
]

web_buttons = [
    'Лабораторні з Web-технології', 'Практичні з Web-технології'
]

it_buttons = [
    'Лабораторна №1 з ІТ', 'Лабораторна №2 з ІТ',
    'Лабораторна №3 з ІТ', 'Лабораторна №4 з ІТ',
    'Лабораторна №5 з ІТ', 'Лабораторна №6 з ІТ',
    'Лабораторна №7 з ІТ', 'Лабораторна №8 з ІТ',
]

idz_hight_math_buttons = [
    'ІДЗ №1', 'ІДЗ №2',
    'ІДЗ №3', 'ІДЗ №4',
    'ІДЗ №5'
]

instruction_buttons = [
    'Ціни',
    'Як оформити правильно заказ?',
    'Оплата'
]
