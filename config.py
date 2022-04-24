# Importing required Libaries
import os 
import telebot
from flask import Flask, request
import requests
from dotenv import load_dotenv

load_dotenv()


# Logging Setup
import logging
logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
    )


TOKEN = os.getenv('TOKEN')

DEBUG = True

SERVER_URL = os.getenv("SERVER_URL")




bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

import importdir
importdir.do("utils", globals())







