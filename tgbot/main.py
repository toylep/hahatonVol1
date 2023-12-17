from dotenv import load_dotenv
import os
import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
import requests
import uuid
import string
import random
load_dotenv()
from flask import Flask
app = Flask(__name__)
TOKEN = os.environ.get('BOT_TOKEN')
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

dp = Dispatcher()

@app.post('/spam')
def spam(message:str):
    bot.send_message(message)
    return "200"




def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string

@dp.message(CommandStart())
async def start_command(message:types.Message):
    await message.answer('Привет для тебя есть следующие команды: \n /log_devrel\n /log_developer')

@dp.message()
async def developer_reg(message:types.Message):
    token = generate_random_string(6)
    await message.answer('Подождите,скоро вам придет токен')
    print()
    if message.text == '/log_developer':
        requests.post(
            url='http://localhost:8000/comm/reg/',
            data={
                "username": message.chat.username,
                "first_name": message.chat.first_name,
                "last_name": message.chat.last_name
            }
        )
        requests.post(
            url='http://localhost:8000/comm/session/',
            data={
                "username": message.chat.username,
                "token" : token
            }
        )
        await message.answer(token)

    if message.text =='/log_devrel':
        requests.post(
            url='http://localhost:8000/comm/reg/',
            data={
                "username": message.chat.username,
                "first_name": message.chat.first_name,
                "last_name": message.chat.last_name
            }
        )
        requests.post(
            url='http://localhost:8000/comm/session/',
            data={
                "username": message.chat.username,
                "token" : token
            }
        )
        await message.answer(token)

async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.create_task(asyncio.to_thread(app.run()))
    asyncio.run(main())
    