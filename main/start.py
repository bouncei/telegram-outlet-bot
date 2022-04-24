import types
from config import *


def menu(msg):
    """
    The first pop-up menu after initializing the bot    
    """
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    a = types.KeyboardButton("🛒 Store")
    b = types.KeyboardButton("🛍 Orders")
    c = types.KeyboardButton("💳 Wallet")
    d = types.KeyboardButton("📞 Support")

    keyboard.add(a, b, c, d)

    return keyboard


@bot.message_handler(commands=['start'])
def start(msg):
    """ 
    Ignites the bot application to take action

    """

    bot.reply_to(
        msg,
        "Welcome to the Telegram Outlet Bot",
        reply_markup=menu(msg)
    )
