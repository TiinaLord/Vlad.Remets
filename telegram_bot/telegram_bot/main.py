import telebot
from telebot import types

bot = telebot.TeleBot("6272916393:AAEf5FRKbPC2CXKq0cIhitUpmHOFyaYbBOU")

@bot.message_handler(commands=["start"])
def start(message):
    mess = f"Приветствую тебя, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>"
    bot.send_message(message.chat.id, mess, parse_mode="html")

# @bot.message_handler(content_types=["text"])
# def get_user_text(message):
#     if message.text == "Hello":
#         bot.send_message(message.chat.id, "Hi!!", parse_mode="html")
#     elif message.text == "id":
#         bot.send_message(message.chat.id, f"Here is your id: {message.from_user.id}", parse_mode="html")
#     elif message.text == "photo":
#         photo = open("900834.png", "rb")
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, "I don't understand you, can you repeat your request? :)", parse_mode="html")

@bot.message_handler(content_types=["photo"])
def get_user_photo(message):
    bot.send_message(message.chat.id, "Not bad, not bad, but why are sending me your photos?")

@bot.message_handler(commands=["video"])
def video(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Тапай", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley"))
    bot.send_message(message.chat.id, "Наслаждайся просмотром!", reply_markup=markup)


@bot.message_handler(commands=["help"])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    help = types.KeyboardButton("Help")
    restart = types.KeyboardButton("/start")
    markup.add(help, restart)
    bot.send_message(message.chat.id, "HA, i can't help you and the button help don't work correctly, push restart", reply_markup=markup)

bot.polling(none_stop=True)