#!/usr/bin/env bash
"$VIRTUAL_ENV/bin/uwsgi" --http=:8080 --wsgi-file=run_connexion.py "--virtualenv=$VIRTUAL_ENV"