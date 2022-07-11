import logging
import os
from logging.handlers import RotatingFileHandler

import requests
from dotenv import load_dotenv
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from telegram import Bot, KeyboardButton, ReplyKeyboardMarkup

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


def send_number(phone_number, username):
    url = 'https://s1-nova.ru/app/private_test_python/'
    json = {'phone': phone_number, 'login': username}
    try:
        response = requests.post(url=url, json=json)
        logger.info('отправили номер ' + phone_number + ' для пользователя ' + username)
        with open('numbers_sent.txt', 'a', encoding="utf-8") as f:
            f.write(phone_number + ' ' + username + '\n')
    except Exception as error:
        logger.error(f'Ошибка при запросе к API: {error}')


def wake_up(chat_id):
    with open('bot_message.txt', 'r', encoding="utf-8") as f:
        text = f.read()
    button = KeyboardButton(
        text='Отправить номер',
        request_contact=True
    )
    buttons = ReplyKeyboardMarkup([
        [button, ], ],
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

    username = request.data.get('message', {}).get('chat', {}).get('username', {})
    phone_number = request.data.get('message', {}).get('contact', {}).get('phone_number', {})
    if (message_id == 1 and message_text == '/start') or message_text == '/initialize':
        wake_up(chat_id)
    if phone_number:
        send_number(phone_number, username)
    return Response(status=status.HTTP_200_OK)
