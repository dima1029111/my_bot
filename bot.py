import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

import os

TOKEN = "8877648136:AAHHzSPLa93Mf_-PSyyPprECskTV3-0kLa4"
if not TOKEN:
    print("Ошибка: Переменная TELEGRAM_TOKEN не найдена!")
    exit()

bot = telebot.TeleBot(TOKEN)

CHANNEL_1 = "@robloxxzoaiii3"
CHANNEL_2 = "@robloxxxzai"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.chat.id
    
    # Создаём кнопки
    keyboard = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton("📢 ПОДПИСАТЬСЯ НА КАНАЛ 1", url=f"https://t.me/{CHANNEL_1[1:]}")
    btn2 = InlineKeyboardButton("📢 ПОДПИСАТЬСЯ НА КАНАЛ 2", url=f"https://t.me/{CHANNEL_2[1:]}")
    check_btn = InlineKeyboardButton("🔍 ПРОВЕРИТЬ ПОДПИСКИ", callback_data="check")
    keyboard.add(btn1, btn2, check_btn)
    
    # Отправляем ОДНО сообщение (каждый раз новое)
    bot.send_message(
        user_id,
        "🎉 ПРИВЕТ! 🎉\n\n"
        "Чтобы забрать 25 000 Робуксов БЕСПЛАТНО,\n"
        "нужно выполнить 2 очень простых задания!\n\n"
        "👇 Подпишись на каналы ниже 👇",
        reply_markup=keyboard
    )

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == "check":
        bot.answer_callback_query(call.id, "✅ Проверка подписок (скоро добавим)")

from flask import Flask
import threading



if __name__ == "__main__":
    print("🤖 Бот запущен...")
    bot.infinity_polling()
