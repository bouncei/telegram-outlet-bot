from config import *
from models import *


def get_user(msg):
    """
    Returns an existing user, else create a new user
    """
    id = msg.from_user.id

    user = session.query(User).filter_by(id=id).first()

    if user:
        return user

    else:
        user = User(id=id, balance="0", mnemonic="",  order=0)
        session.add(user)
        session.commit(user)

        return user
