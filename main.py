import telebot as tb
import telebot.types as ktb

# Создание подключения к телеграм-боту
API_KEY = "8009374664:AAGxw22pjSD0B8WZUX6zBcWcsFgddKI0fpw"
bot = tb.TeleBot(API_KEY)

# Обработчики
@bot.message_handler(commands=['start'])
def comand_start(message):
  bot.send_message(
    chat_id=message.chat.id,
    text="Start",
    parse_mode="Markdown"
  )


# polling чтобы бот постоянно работал
bot.polling()