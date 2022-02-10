import logging

from aiogram import executor, types, Bot, Dispatcher

from create_bot import dp, bot
from config import OWNER

logging.basicConfig(format = u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level = logging.INFO)

from handlers import *

from navigation import *

from admins_handlers import *

from orders import *

# ------------------------------Handlers-------------------------------------- #

handler_price_programming.register_handlers_price_programming(dp)
handler_price_IT.register_handlers_price_IT(dp)
handler_price_hight_math.register_handlers_price_hight_math(dp)
handler_price_english.register_message_handler_english(dp)

# ------------------------------Navigation-------------------------------------- #

look_price.register_handlers_see_price(dp)
start.register_handlers_start_command(dp)
choose_lab.register_handlers_choose_lab(dp)
info_about_creaters.register_handlers_informations(dp)
back_to_menu.register_handlers_back_to_menu(dp)
coming_soon.register_handlers_coming_soon(dp)
how_to_used.register_handler_how_to_used_bot(dp)
feedback.register_message_handler_feedback(dp)

# ------------------------------Orders-------------------------------------- #

create_order_programming.register_handlers_programming(dp)
create_order_math.register_handlers_math(dp)
create_order_it.register_handlers_create_it(dp)
create_order_english.register_message_handler_create_order_english(dp)
application_akj.register_message_handler_get_applications(dp)

# ------------------------------Admins handlers-------------------------------------- #

test_func.register_handlers_test(dp)
notification_all.register_handlers_rozsilaca_messages(dp)
random_choice.register_handlers_choice_winner(dp)

# -------------------------------------------------------------------- #

async def on_start_bot(dp: Dispatcher):
    try:
        await dp.bot.send_message(OWNER, 'Bot started!')
        await set_commands(bot)
    except Exception as e:
        logging.exception(e)

async def set_commands(bot: Bot):
    await bot.set_my_commands([
        types.BotCommand(command = '/start', description = 'Старт'),
        types.BotCommand(command = '/back', description = 'Відмінити створення заказу'),
        types.BotCommand(command = '/feedback', description = 'Відправити нам Ваш Feedback ^^')
    ])

executor.start_polling(dp, skip_updates = True, on_startup = on_start_bot)