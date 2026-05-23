import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# --- Получение токена ---
TOKEN = os.environ.get("TELEGRAM_TOKEN")
if not TOKEN:
    print("Ошибка: Переменная TELEGRAM_TOKEN не найдена!")
    exit()

bot = telebot.TeleBot(TOKEN)
print("✅ Токен загружен, запускаю бота...")

# --- Настройки каналов (ЗАМЕНИТЕ НА СВОИ) ---
CHANNEL_1 = "@robloxxzoaiii3"
CHANNEL_2 = "@robloxxxzai"


# --- Команда /start ---
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.chat.id
    keyboard = InlineKeyboardMarkup(row_width=1)

    btn1 = InlineKeyboardButton("📢 КАНАЛ 1", url=f"https://t.me/{CHANNEL_1[1:]}")
    btn2 = InlineKeyboardButton("📢 КАНАЛ 2", url=f"https://t.me/{CHANNEL_2[1:]}")
    check_btn = InlineKeyboardButton("🔍 ПРОВЕРИТЬ", callback_data="check")
    keyboard.add(btn1, btn2, check_btn)

    bot.send_message(
        user_id,
        "🎉 ПРИВЕТ! 🎉\n\nЧтобы получить 25 000 Робуксов, подпишись на каналы ниже и нажми «ПРОВЕРИТЬ».",
        reply_markup=keyboard
    )

# --- Обработка нажатия на кнопку "ПРОВЕРИТЬ" ---
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == "check":
        bot.answer_callback_query(call.id, "✅ Проверка подписок скоро заработает!")

# --- Запуск бота ---
if __name__ == "__main__":
    print("🤖 Бот запущен и готов к работе!")
    bot.infinity_polling()
