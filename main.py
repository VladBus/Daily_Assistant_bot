# -*- coding: utf-8 -*-
from bot.utils.config import bot
from bot.handlers import basic
from bot.handlers import text

print("Бот запущен...")
bot.polling(none_stop=True)
print("Бот остановлен...")
