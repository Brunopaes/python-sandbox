# -*- coding: utf-8 -*-
from morse_processing import morse_parser

import telebot
import json
import os


path = \
    os.path.abspath('{}/misc/settings.json'.
                    format(os.getcwd() + os.sep + os.pardir))

API_TOKEN = json.loads(open(path, 'r').read())['API_TOKEN']

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    """This function gets the incoming message and replies with it.
    Parameters
    ----------
    message : telebot.types.Message
        The message object.
    """
    bot.send_message(message.chat.id, morse_parser(message.text))


bot.polling()
