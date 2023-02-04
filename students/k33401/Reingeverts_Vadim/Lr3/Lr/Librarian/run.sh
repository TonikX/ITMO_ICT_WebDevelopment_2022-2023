#!/bin/bash 
# Makes it so it doesn't matter from which directory script is called
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P ) # https://stackoverflow.com/a/24112741
cd "$parent_path"

# If there are arguments provided, pass them to the `manage.py`
if [ -z "$1" ] # https://stackoverflow.com/a/19486205
  then
    # Migrates and runs dev server
    source ../../../.web-dev-env/Scripts/activate && python manage.py tailwind start &
    source ../../../.web-dev-env/Scripts/activate && python manage.py makemigrations && python manage.py migrate && python manage.py runserver
else
    source ../../../.web-dev-env/Scripts/activate && python manage.py "$@"
fi
