import os

from aiogram import Dispatcher
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))
dp = Dispatcher()
