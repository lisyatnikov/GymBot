#TODO make reconnection
import config
import telebot


from database_control import add_pushups, set_connection_database
from database_control import monkey_func
from telebot import types

bot = telebot.TeleBot(config.BOT_TOKEN)


def func(exception_code):
    pass


def main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_add = types.KeyboardButton("Add a number of push-ups")
    btn_weekstat = types.KeyboardButton("Show week progress")
    btn_top5 = types.KeyboardButton("Top-5")
    markup.add(btn_add, btn_weekstat, btn_top5)
    bot.send_message(message.chat.id,
                     text="Hi, {0.first_name}! I am your fitness trainer".format(message.from_user),
                     reply_markup=markup)




@bot.message_handler(commands=['start','help'])
def start(message):
    main_menu(message)


# @bot.message_handler(content_types=['text'])
# def read_pushups(message):
#     result = message.text
#     result = int(result)
#     add_pushups(result)
#

@bot.message_handler(func=lambda message: (message.text in
                                           ["Add a number of push-ups", "Show week progress", "Top-5", "Main menu"]))
def click_handling(message):
    if message.text == "Add a number of push-ups":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_back = types.KeyboardButton("Main menu")
        #TODO:read_pushups(message)
        markup.add(btn_back)
        bot.send_message(message.chat.id,
                         text="how many pushups have you done today? Add number and press send or ENTER",
                         reply_markup=markup)
    elif message.text == "Show week progress":
        func(exception_code)
    elif message.text == "Top-5":
        pass
    elif message.text == "Main menu":
       main_menu(message)
    else:
        bot.send_message(message.chat.id, text="ERROR 418: I am not a coffee maker!")

@bot.message_handler(content_types=['text']) #TODO: input values has be a number!!!
def read_pushups(message):
    result = message.text
    result = int(result)
    add_pushups(result)

    #bot.send_message(message.chat.id, result)

bot.polling()
