import telebot as tb
from func_and_slova import genereted

# Создание подключения к телеграм-боту
API_KEY = "8178906764:AAGIGxBpg26shPHTWB17H4OAPUnrt_DL4LM"
bot = tb.TeleBot(API_KEY)

# Обработчики
@bot.message_handler(commands=['start'])
def comand_start(message):
  bot.send_message(
    chat_id=message.chat.id,
    text="Привет это телеграм бот, который генерирует случайную историю по команде /story.",
    parse_mode="Markdown"
  )
@bot.message_handler(commands=['story'])
def comand_story(message):
    # Вызов функции из другого файла
    sentence = genereted()
    bot.send_message(
        chat_id=message.chat.id,
        text=sentence,
        parse_mode="Markdown"
    )

# polling чтобы бот постоянно работал
bot.polling()