#!/bin/bash
set -eux
python manage.py collectstatic --noinput
uwsgi --ini /srv/uwsgi.ini

