#!/usr/bin/env python

from app import create_app
from os import getenv


listen_port = getenv('LISTEN_PORT', 8080)

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=listen_port)
