from config import *
from utils import *


@bot.message_handler(regexp="^🛍 Orders")
def store(msg):
    """
    Reply when the order Category is selected
    """

    user = get_user(msg)
    print(user)

    bot.send_message(
        msg.from_user.id,
        "What can we help you do today? Please explain it to us here ...",
    )

    bot.reply_to(
        msg,
        f"You just successfully added a new user to the sqlalchemy database with the id, {user.id}",

    )
