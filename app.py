from flask import Flask, request
import telepot
import sys
from wow_token_price_fetcher import get_token_price
from loguru import logger



bot = telepot.Bot('key')

bot.setWebhook("https://py-wowtokenprice.herokuapp.com/", max_connections=1)

app = Flask(__name__)

@logger.catch
@app.route('/', methods=["POST"])
def telegram_webhook():
    try:
        update = request.get_json()
        if "message" in update:
            text = update["message"]["text"]
            chat_id = update["message"]["chat"]["id"]
            if text == 'price':
                bot.sendMessage(chat_id,f"Current Price {get_token_price()}")
            else:
                bot.sendMessage(chat_id, "From the web: you said '{}'".format(text))
        return "OK"
    except:
        logger.info("Unexpected error:{sys.exc_info()[0]}")
        print(f"Unexpected error:{sys.exc_info()[0]}")
    return 503     

if __name__ == '__main__':
    logger.start("loguru.log")
    app.run(debug=True, use_reloader=True)