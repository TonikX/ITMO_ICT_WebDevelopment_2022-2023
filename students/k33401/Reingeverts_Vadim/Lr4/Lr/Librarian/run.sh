#!/bin/bash 
# Makes it so it doesn't matter from which path script is called
script_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P ) # https://stackoverflow.com/a/24112741
cd "$script_path"

# Path to python venv
source ../../../.web-dev-env/Scripts/activate 

# Server ports
backend_port=8000
frontend_port=3000

# Exported as an environment variable
# Can be accessed in django template like this:
#
#   {% load env_utils %}
#
#   {{ "backend_port"|get_env }}
#   {{ "frontend_port"|get_env }}
#
export backend_port=$backend_port
export frontend_port=$frontend_port



# Migrates, and then runs dev backend server in parrallel to runs frontend server
if [ -z "$1" ] # https://stackoverflow.com/a/19486205
then
    python manage.py makemigrations && python manage.py migrate && python manage.py runserver $backend_port &
    cd frontend && npm run dev -- --port $frontend_port
# If first argument is npm, then following arguments to the npm of the frontend
elif [ $1 == "npm" ]
then
    cd frontend && echo "$PWD" && "$@"
# If there are non-npm arguments provided, pass them to the `manage.py`
else
    python manage.py "$@"
fi

# python manage.py collectstatic