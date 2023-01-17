#!/bin/bash 

source ../../../.web-dev-env/Scripts/activate && python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000 &
source ../../../.web-dev-env/Scripts/activate && python manage.py tailwind start 