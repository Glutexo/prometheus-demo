#!/usr/bin/env python

from app.flask import create_app
from os import getenv
from werkzeug.serving import run_simple


listen_port = getenv('LISTEN_PORT', 8080)
application = create_app()

if __name__ == "__main__":
    # application.run(host="0.0.0.0", port=listen_port)
    run_simple("0.0.0.0", listen_port, application)
