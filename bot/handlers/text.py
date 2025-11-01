# -*- coding: utf-8 -*-
from bot.utils.config import bot


@bot.message_handler()
def info(message):
    """
        Обработчик для обработки входящих сообщений от пользователей.
        Реагирует на определенные команды персонализированными сообщениями.
    """
    if message.text.lower() == 'hello':
        # If the message is 'hello' (case-insensitive), send a greeting with user's first and last name
        bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name} {message.from_user.last_name}!')
    elif message.text.lower() == 'id':
        # If the message is 'id' (case-insensitive), reply with the user's ID
        bot.reply_to(message, f'ID: {message.from_user.id}')
