# REST API погоды

### Установка

Создание виртуалльного окружения и все настройки:
```commandline
python -m venv venv
venv\Scripts\activate
python manage.py migrate
python manage.py createsuperuser
```

Загрузка городов в базу данных
```commandline
python manage.py loaddata data.json
```

### Документация API
`/api/cities` (GET) - список городов

Пример конкретного города:
```json
{
  "id": 1,
  "name": "Санкт-Петербург",
  "description": "Город на Неве",
  "lat": 59.9375,
  "lon": 30.308611,
  "country": "ru"
}
```

`/api/countries` (GET) - список стран + городов в них

Пример конкретной страны:
```json
{
  "code": "us",
  "cities": [
    {
      "id": 3,
      "name": "Нью-Йорк",
      "description": "Большое яблоко",
      "lat": 40.73061,
      "lon": -73.935242,
      "country": "us"
    },
    {
      "id": 4,
      "name": "Лос-Анджелес",
      "description": "Там находится Голливуд",
      "lat": 34.052235,
      "lon": -118.243683,
      "country": "us"
    }
  ],
  "name": "США"
}
```

`/api/choices` (GET, POST, PUT, PATCH, DELETE) - города, выбранные пользователем

Пример списка выбранных городов:
```json
[
  {
    "id": 3,
    "city": {
      "id": 1,
      "name": "Санкт-Петербург",
      "description": "Город на Неве",
      "lat": 59.9375,
      "lon": 30.308611,
      "country": "ru"
    }
  },
  {
    "id": 4,
    "city": {
      "id": 2,
      "name": "Москва",
      "description": "Столица РФ",
      "lat": 55.755826,
      "lon": 37.6173,
      "country": "ru"
    }
  },
  {
    "id": 5,
    "city": {
      "id": 7,
      "name": "Сыктывкар",
      "description": "Тут очень холодно",
      "lat": 61.666668,
      "lon": 50.816666,
      "country": "ru"
    }
  }
]
```