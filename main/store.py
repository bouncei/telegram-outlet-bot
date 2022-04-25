from config import *
from utils import *


def storeCategory(msg):
    """
    Listing out all products in the store

    """
    prod = ['josh', 'jane', "alpha"]  # Getting products for the a .json file

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = []

    # Looping throgh the array of produts and making it an indivdual button each
    for i in prod:
        key = types.InlineKeyboardButton(
            text=f"{i}", callback_data="Listed Item", url="google.com")
        buttons.append(key)

        keyboard.add(key)

    # print(buttons)
    return keyboard


@bot.message_handler(regexp="^🛒 Store")
def store(msg):
    """
    Reply when the store Category is selected
    """

    bot.reply_to(
        msg,
        "You just successfully selected the Store category",
        reply_markup=storeCategory(msg)

    )
