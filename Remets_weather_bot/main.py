import telebot
import requests
import json

bot = telebot.TeleBot("6288131973:AAHsJBIe1Dwf-dniMvVbesuPsA5UBR5BazY")
API = "c3d3561fa82aa9ef1a69230847d1eb1f"

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Hello, choose your city!")

@bot.message_handler(content_types=["text"])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?id={city}&appid={API}&units=metric")
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data['main']["temp"]
        bot.reply_to(message, f'Текущая погода: {temp}')

        image = "sunny.png" if temp > 5.5 else "rainy.png"
        file = open("./" + image, "rb")
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, "invalid request, check your message and try again")

bot.polling(none_stop=True)
