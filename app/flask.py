from app import index
from flask import Flask


def create_app():
    flask_app = Flask(__name__)
    flask_app.add_url_rule("/", view_func=index)
    return flask_app
