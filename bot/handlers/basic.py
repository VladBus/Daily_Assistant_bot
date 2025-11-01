# -*- coding: utf-8 -*-
from bot.utils.config import bot
import webbrowser


# Это декоратор, который регистрирует функцию в качестве обработчика сообщений для команд /start и /main
@bot.message_handler(commands=['start', 'main'])
def send_welcome(message):
    # Отправить приветственное сообщение пользователю с указанием его имени и фамилии
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name} {message.from_user.last_name}!')


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, '<b>help</b> <em><u>information</u></em>', parse_mode='HTML')


# @bot.message_handler(commands=['site'])
# def send_site(message):
#     # Важно: webbrowser.open откроет сайт на СЕРВЕРЕ, где запущен бот, а не у пользователя!
#     # Это скорее всего не то, что вы хотите. Для отправки ссылки используйте:
#     bot.send_message(message.chat.id, "Вот ссылка на сайт: https://www.google.com")


@bot.message_handler(commands=['site'])
def send_site(message):
    webbrowser.open('https://www.google.com')
