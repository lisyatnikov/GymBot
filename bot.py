#TODO make reconnection
import config
import telebot


from database_control import add_pushups, set_connection_database
from database_control import monkey_func
from telebot import types

bot = telebot.TeleBot(config.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_add = types.KeyboardButton("Add a number of push-ups")
    btn_weekstat = types.KeyboardButton("Show week progress")
    btn_top5 = types.KeyboardButton("Top-5")
    markup.add(btn_add, btn_weekstat, btn_top5)
    bot.send_message(message.chat.id,
                     text="Hi, {0.first_name}! I am your fitness trainer".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def click_handling(message):
    if message.text == "Add a number of push-ups":
        bot.send_message(message.chat.id, text="Cool!")
    elif message.text == "Show week progress":
        pass
    elif message.text == "Top-5":
        pass
    else:
        bot.send_message(message.chat.id, text="ERROR 418: I am not a coffee maker!")


# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.send_message(message.chat.id, "Hello")

@bot.message_handler(content_types=['text'])
def read_pushups(message):
    result = message.text
    result = int(result)
    add_pushups(result)



    #bot.send_message(message.chat.id, result)

bot.polling()
