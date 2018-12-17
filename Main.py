from flask import Flask, request, render_template, abort
import telepot
from wow_token_price_fetcher import get_token_price
from dotenv import load_dotenv
import os
import sentry_sdk
from sentry_sdk import capture_exception, capture_message

load_dotenv(verbose=True)
SECRET = os.getenv('SECRET')
BOTKEY = os.getenv('BOTKEY')
SENTRYCONF = os.getenv('SENTRYCONF')

bot = telepot.Bot(BOTKEY)
bot.setWebhook("https://deliciouswarmastronomy--lairdstreak93.repl.co/", max_connections=1)

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index(name=None):
    return render_template('index.htm', name=name)    

@app.route('/', methods=["POST"])
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

if __name__ == '__main__':
    sentry_sdk.init(SENTRYCONF)
    app.run(host='0.0.0.0', port='3000')
