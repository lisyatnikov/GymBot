#TODO make reconnection
import config
import telebot

from database_control import add_pushups, set_connection_database
from database_control import monkey_func
from telebot import types

bot = telebot.TeleBot(config.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hello")

@bot.message_handler(content_types=['text'])
def read_pushups(message):
    result = message.text
    result = int(result)
    add_pushups(result)


    #bot.send_message(message.chat.id, result)

bot.polling()
