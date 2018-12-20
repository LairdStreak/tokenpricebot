from flask import Flask, render_template
from dotenv import load_dotenv
import os
import sentry_sdk
from sentry_sdk import capture_exception, capture_message
from botapi import botapi

load_dotenv(verbose=True)
SECRET = os.getenv('SECRET')
BOTKEY = os.getenv('BOTKEY')
SENTRYCONF = os.getenv('SENTRYCONF')

app = Flask(__name__)

app.register_blueprint(botapi, url_prefix='/api')

@app.route('/', methods=["GET"])
def index():
    return render_template('index.htm', name='Joe Blogs')

if __name__ == '__main__':
    sentry_sdk.init(SENTRYCONF)
    app.run(debug=True)