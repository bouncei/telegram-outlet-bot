# Importing required Libaries
import importdir
import logging
import os
import telebot
from telebot import types
from flask import Flask, request
import requests
from dotenv import load_dotenv

# python liberies for sql ORM config
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import sessionmaker


load_dotenv()

# Logging Setup
logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
)


TOKEN = os.getenv('TOKEN')

DEBUG = True

SERVER_URL = os.getenv("SERVER_URL")

DATABASE_URI = os.getenv("DATABASE_URI")

print(DATABASE_URI)

# Database configuration
Base = declarative_base()
engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine, autoflush=False)


bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

importdir.do("utils", globals())
