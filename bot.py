import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hello")


@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("AddPushups")
    markup.add(item1)

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "AddPushups":
        bot.send_message(message.chat.id, "https://habr.com/ru/users/lubaznatel/")


bot.infinity_polling()
