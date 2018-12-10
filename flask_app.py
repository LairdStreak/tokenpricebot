from flask import Flask, request
import telepot
import urllib3
from wow_token_price_fetcher import get_token_price

proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))

secret = "4ae627b7-c449-4357-a12e-eeac315db799"

bot.setWebhook("https://YOUR_PYTHONANYWHERE_USERNAME.pythonanywhere.com/{}".format(secret), max_connections=1)

app = Flask(__name__)

@app.route('/{}'.format(secret), methods=["POST"])
def telegram_webhook():
    update = request.get_json()
    if "message" in update:
        text = update["message"]["text"]
        chat_id = update["message"]["chat"]["id"]
        if text == 'price':
            bot.sendMessage(chat_id,f"Current Price {get_token_price()}")
        else:
            bot.sendMessage(chat_id, "From the web: you said '{}'".format(text))
    return "OK"
