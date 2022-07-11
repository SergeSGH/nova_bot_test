from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import requests
import logging
# from telegram.ext import Updater, Filters, MessageHandler
# from telegram.ext import CommandHandler
from telegram import Bot, ReplyKeyboardMarkup, KeyboardButton
from logging.handlers import RotatingFileHandler

import os
from dotenv import load_dotenv
load_dotenv()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler(
    'my_logger.log',
    maxBytes=50000000,
    backupCount=5
)
logger.addHandler(handler)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
handler.setFormatter(formatter)

bot = Bot(token=os.getenv('TELEGRAM_TOKEN'))


def send_number(phone_number, login):
    
    url = 'https://s1-nova.ru/app/private_test_python/'
    json = {'phone': phone_number,'login': login }

    try:
        response = requests.get('https://api.thecatapi.com/v1/images/search')
        # response = requests.post(url=url, json=json)
    except Exception as error:
        logger.error(f'Ошибка при запросе к API: {error}')
    logger.info('отправили номер ' + phone_number + 'для пользователя ' + login)


def say_hi(update, context):
    chat = update.effective_chat
    with open('bot_message.txt', 'r', encoding="utf-8") as f:
        text = f.read()
    try:
        context.bot.send_message(chat_id=chat.id, text=text)
    except Exception as error:
        logger.error(f'Ошибка при запросе к API Telegram: {error}')


def wake_up(chat_id):
    with open('bot_message.txt', 'r', encoding="utf-8") as f:
        text = f.read()
    button = KeyboardButton(
        text='Отправить номер', 
        request_contact=True
    )
    buttons = ReplyKeyboardMarkup([
        [button,],],
        resize_keyboard=True
    )
    bot.send_message(
        chat_id=chat_id,
        text=text,
        reply_markup=buttons
    )


@api_view(['POST'])  
def bot_data(request):
    with open('request_data.txt', 'w', encoding="utf-8") as f:
        f.write(str(request.data))
    message_id = request.data.get('message', {}).get('message_id', {})
    message_text = request.data.get('message', {}).get('text', {})
    chat_id = request.data.get('message', {}).get('chat', {}).get('id', {})
    if message_id == 17 and message_text == '/start':
        wake_up(chat_id)
    # with open('numbers_sent.txt', 'a', encoding="utf-8") as f:
    #     f.write(str(number) + '\n')
    return Response(status=status.HTTP_200_OK)
