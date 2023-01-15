# Lab work 2. Implementation of a simple website on django.

## General

### Activating python venv

```bash
source ../.web-dev-env/Scripts/activate
```

### VSCode setup

`Python: Select Interpreter` – to fix IntelliSense

```bash
python -m pip install --upgrade djlint
```

Install djlint extension and add its config - `.djlintrc`:

```json
{
    "ignore": "H030,H031"
}
```

### Running

```bash
python django_project_reingeverts/manage.py makemigrations && python django_project_reingeverts/manage.py migrat e && python django_project_reingeverts/manage.py runserver
```

### Admin

User: `admin`

Email: `admin@example.com`

Password: `admin`

## Practical part

### Practical work 2.1.1-2.1.5

Model
![](https://i.imgur.com/60P88U7.png)

View
![](https://i.imgur.com/G0y3Vvm.png)

### Practical work 2.2.1-2.2.2

![](https://i.imgur.com/cRPpsFy.gif)

### Practical work 2.2.3

![](https://i.imgur.com/vwzqnWc.gif)

## Lab work part

...
