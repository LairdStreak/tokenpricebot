from flask import Flask, request
import telepot
import sys
from wow_token_price_fetcher import get_token_price
from loguru import logger
from dotenv import load_dotenv
from werkzeug import exceptions
import os
load_dotenv(verbose=True)
SECRET = os.getenv('SECRET')
BOTKEY = os.getenv('BOTKEY')

bot = telepot.Bot(BOTKEY)
bot.setWebhook("https://deliciouswarmastronomy--lairdstreak93.repl.co/", max_connections=1)

app = Flask(__name__)

@app.errorhandler(exceptions.BadRequest)
def handle_bad_request(e):
    return 'bad request!', 400

@app.errorhandler(exceptions.InternalServerError)
def handle_server_error(e):
    return 'internal server error ...', 500    

@app.route('/', methods=["POST"])
def telegram_webhook():
    try:
        update = request.get_json()
        logger.info(update)
        if "message" in update:
            text = update["message"]["text"]
            chat_id = update["message"]["chat"]["id"]
            if text == 'price':
                bot.sendMessage(chat_id,f"Current Price {get_token_price()}")
            else:
                bot.sendMessage(chat_id, "From the web: you said '{}'".format(text))
        return "OK"
    except Exception as e:
        logger.error(f"Unexpected error:{e}")

if __name__ == '__main__':
    logger.start("loguru.log")
    #host=0.0.0.0
    app.run(port='3000')
