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

### Practical work 2.3

![](https://i.imgur.com/FlRST5k.png)

## Lab work part

> 17 mod 7 = 3

3. Табло отображения информации об авиаперелетах.
   Хранится информация о номере рейса, авиакомпании, отлете, прилете, типе (прилет, отлет), номере гейта.
   Необходимо реализовать следующий функционал:

- [x] Регистрация новых пользователей.
- [ ] Просмотр и резервирование мест на рейсах. Пользователь должен иметь возможность редактирования и удаления своих резервирований.
- [ ] Администратор должен иметь возможность зарегистрировать на рейс пассажира и вписать в систему номер его билета средствами Django-admin.
- [ ] В клиентской части должна формироваться таблица, отображающая всех пассажиров рейса.
- [ ] Написание отзывов к рейсам. При добавлении комментариев, должны сохраняться дата рейса, текст комментария, рейтинг (1-10), информация о комментаторе.

...

### Requirements

geocoder
requests_cache
django-money


### Running

Script for running dev server with tailwinds,

```bash
bash run.sh
```

which combines this:

```bash
source ../../../.web-dev-env/Scripts/activate && python manage.py makemigrations && python manage.py migrate && python manage.py runserver
```

and that command:

```bash
source ../../../.web-dev-env/Scripts/activate && python manage.py tailwind start
```
