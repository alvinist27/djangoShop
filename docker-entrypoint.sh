#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata app_users/fixtures/01_users_fixture.json

exec "$@"
