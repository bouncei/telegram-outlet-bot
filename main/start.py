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


# @bot.message_handler(commands=['store'])
# def help_command(message):
#     keyboard = telebot.types.InlineKeyboardMarkup()
#     keyboard.add(
#         telebot.types.InlineKeyboardButton(
#             text="Message the developer", url='telegram.me/artiomtb'
#         )
#     )
#     bot.send_message(
#         message.chat.id,
#         '1) To receive a list of available currencies press /exchange.\n' +
#         '2) Click on the currency you are interested in.\n' +
#         '3) You will receive a message containing information regarding the source and the target currencies, ' +
#         'buying rates and selling rates.\n' +
#         '4) Click “Update” to receive the current information regarding the request. ' +
#         'The bot will also show the difference between the previous and the current exchange rates.\n' +
#         '5) The bot supports inline. Type @<botusername> in any chat and the first letters of a currency.',
#         reply_markup=keyboard
#     )
