#!/bin/bash 
# Makes it so it doesn't matter from which path script is called
script_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P ) # https://stackoverflow.com/a/24112741
cd "$script_path"

# Path to python venv
source ../../../.web-dev-env/Scripts/activate 

# Server ports
backend_port=8000
frontend_port=3000
# host="192.168.1.246"
host="localhost"

# Exported as an environment variable
export backend_port=$backend_port
export frontend_port=$frontend_port
export host=$host

# Migrates, and then runs dev backend server in parrallel to runs frontend server
if [ -z "$1" ] # https://stackoverflow.com/a/19486205
then
    python manage.py makemigrations && python manage.py migrate && python manage.py runserver $host:$backend_port &
    cd frontend && npm run dev -- --host $host --port $frontend_port
# If first argument is npm, then pass following arguments to the npm of the frontend
elif [ $1 == "npm" ]
then
    cd frontend && echo "$PWD" && "$@"
# If first argument is pip, then pass following arguments to the pip of the backend
elif [ $1 == "pip" ]
    echo "$PWD" && "$@"
then
    cd frontend && echo "$PWD" && "$@"
# If there are non-npm arguments provided, pass them to the `manage.py`
else
    python manage.py "$@"
fi