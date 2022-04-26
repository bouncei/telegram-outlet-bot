from flask import session
from config import *


class User(Base):
    """
    SqlAlchemy ORM for Users
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    balance = Column(String(15))
    address = Column(String(50))
    order = Column(Integer)
    mnemonic = Column(String(100))

    def __repr__(self):
        return "<User(id='%s')>" % (self.id)


session = Session()

session.close()
