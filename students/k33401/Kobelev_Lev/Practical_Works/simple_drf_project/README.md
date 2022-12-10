# Practical Work 3
Get an idea of how to use the features of serializers in Django Rest Framework.
Simple app about warriors and their jobs & skills.
## Set up the environment
Install node Django and Django Rest Framework
```
$ pip install django
$ pip install djangorestframework
$ pip install drf_yasg
```
## Available scripts
### Start the server
```
$ python manage.py runserver
```
## Available URLs
### Warriors
"X" is a primary key for an object.
```
$ /war/warriors/
$ /war/warriors/X/
$ /war/warriors/X/update
$ /war/warriors/X/delete
```
### Jobs
```
$ /war/jobs/
$ /war/jobs/create/
```
### Skills
```
$ /war/skills/
$ /war/skills/create/
```
