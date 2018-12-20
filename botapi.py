from flask import Flask, request, render_template, abort, Blueprint
import telepot
from dotenv import load_dotenv
import os
from sentry_sdk import capture_exception, capture_message

load_dotenv(verbose=True)
SECRET = os.getenv('SECRET')
BOTKEY = os.getenv('BOTKEY')

bot = telepot.Bot(BOTKEY)
bot.setWebhook("https://deliciouswarmastronomy--lairdstreak93.repl.co/api/", max_connections=1)

botapi = Blueprint('botapi', __name__)

@botapi.route('/', methods=["POST"])
def telegram_webhook():
    try:
        update = request.get_json()
        if "message" in update:
            text = update["message"]["text"]
            chat_id = update["message"]["chat"]["id"]
            if "price" in text:
              bot.sendMessage(chat_id,f"Current Price {get_token_price()}")
            elif "top10" in text:
              capture_message(update)
            else:
              bot.sendMessage(chat_id, "From the web: you said '{}'".format(text))
        return "OK"
    except Exception as e:
        capture_exception(e)
    abort(500)