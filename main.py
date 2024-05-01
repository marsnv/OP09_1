#API_TOKEN = '6982046754:AAEmnJgL_VLyAH9xV2jE5jrgqUeGy8MWeuo'
import time

import telebot
from telebot import types
import threading
import datetime

TOKEN = '6982046754:AAEmnJgL_VLyAH9xV2jE5jrgqUeGy8MWeuo'
bot = telebot.TeleBot(TOKEN)

def send_time():
    while True:
        now = datetime.datetime.now()
        time_str = f"Сейчас: {now.hour} часов и {now.minute} минут"
        bot.send_message(chat_id, time_str)
        time.sleep(300)

@bot.message_handler(commands=['start'])
def start_command(message):
    global chat_id
    chat_id = message.chat.id
    bot.send_message(chat_id, "Добро пожаловать! Нажмите на кнопку Меню для дальнейших действий.")
    send_main_menu(message.chat.id)

    threading.Thread(target=send_time).start()

@bot.message_handler(commands=['hello'])
def hello_command(message):
    bot.send_message(message.chat.id, "Привет!")

@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = "Команды:\n/start - Запуск бота\n/hello - Приветствие\n/help - Помощь"
    bot.send_message(message.chat.id, help_text)

def send_main_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Справка')
    itembtn2 = types.KeyboardButton('Сообщения')
    markup.add(itembtn1, itembtn2)
    bot.send_message(chat_id, "Выберите опцию:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Справка')
def info_command(message):
    help_command(message)

@bot.message_handler(func=lambda message: message.text == 'Сообщения')
def messages_command(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Приветствие')
    itembtn2 = types.KeyboardButton('Текущее время')
    itembtn3 = types.KeyboardButton('Досвидания')
    itembtn4 = types.KeyboardButton('Назад')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.send_message(message.chat.id, "Выберите сообщение:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Приветствие')
def greeting_command(message):
    hello_command(message)

@bot.message_handler(func=lambda message: message.text == 'Текущее время')
def current_time_command(message):
    now = datetime.datetime.now()
    bot.send_message(message.chat.id, f"Сейчас: {now.hour} часов и {now.minute} минут")

@bot.message_handler(func=lambda message: message.text == 'Досвидания')
def goodbye_command(message):
    bot.send_message(message.chat.id, "Досвидания")

@bot.message_handler(func=lambda message: message.text == 'Назад')
def back_command(message):
    send_main_menu(message.chat.id)

bot.polling(none_stop=True)