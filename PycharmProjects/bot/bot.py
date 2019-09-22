import os
import telebot
import requests
from flask import Flask, request

token = "618857925:AAGgZ2naSAEs-h8QhD8F3H2UDM1jHoE7pjE"
bot = telebot.TeleBot(token)
params = ["USD"], ["sell"]
server = Flask(__name__)
C = ["Биткоин", "Биток", "биток", "бетховен"]


def cryptocurtancy(message):
    r = requests.get("https://blockchain.info/ru/ticker")
    data = r.json()
    k = "Курс Бетховенов:  " + str(data["USD"]['sell']) + "$"
    bot.send_message(message.chat.id, k)
    return


@bot.message_handler(commands=['start', 'help',"btc"])
def send_welcome(message):
    if message.text == "/start":
        bot.send_message(message.chat.id, "Здарова, " + message.chat.first_name + "!")
    elif message.text == "/help":
        bot.send_message(message.chat.id, "Что случилось,чувак?")
    elif message.text == "/btc":
        cryptocurtancy(message)
    return


@bot.message_handler(content_types=['text'])
def replying(message):
    print(message)
    if 'Как дела?' in message.text:
        bot.send_message(message.chat.id, "Придумываю план по захватыванию кожанных ублюдков!")
        return
    elif message.text in C:
        cryptocurtancy(message)
        return
    elif str(message.from_user.id) == "547432864" and len(message.text)>25:
        bot.send_message(message.chat.id, "Данила,заебал пиздеть, пошли купаться")
    else:
        bot.send_message(message.chat.id, "иди нахуй")


@server.route("/" + token, methods=["POST"])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://evening-reef-16529.herokuapp.com/" + token)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get("POST", 5000)))
