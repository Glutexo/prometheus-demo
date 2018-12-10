#!/usr/bin/env bash
"$VIRTUAL_ENV/bin/gunicorn" --log-level=debug --bind=0.0.0.0:8080 run_flask
