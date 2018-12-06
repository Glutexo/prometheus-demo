from flask import Flask
from prometheus_client import make_wsgi_app
from werkzeug.wsgi import DispatcherMiddleware


def index():
    return "Prómeþeifur!"


def create_app():
    flask_app = Flask(__name__)
    flask_app.add_url_rule("/", view_func=index)

    prometheus_app = make_wsgi_app()
    flask_app.wsgi_app = DispatcherMiddleware(flask_app, {"/metrics": prometheus_app})

    return flask_app
