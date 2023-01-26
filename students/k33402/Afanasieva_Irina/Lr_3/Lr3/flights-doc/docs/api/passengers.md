## Пассажиры - endpoints

### Список пассажиров

**URL** : `passengers/all`

**Method** : `GET`

**Code** : `200 OK`

**Content** : `{[]}`

```json
    {
        "first_name": "Irina",
        "last_name": "Afanasieva"
    },
    {
        "first_name": "Sonya",
        "last_name": "Marmeladova"
    },
    {
        "first_name": "Haruki",
        "last_name": "Murakami"
    },
    {
        "first_name": "Jared",
        "last_name": "Leto"
    },
    {
        "first_name": "Raisa",
        "last_name": "Zakharovna"
    }
```

### Добавление нового пассаржира

**URL** : `passengers/create/`

**Method** : `POST`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "first_name": "",
    "last_name": "",
    "username": "",
    "password": ""
}
```

### Редактирование (get/update/delete) информации о существующем пассажире

**URL** : `passengers/<int:pk>/`

**Method** : `GET`, `PUT`, `PATCH`, `DELETE`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "first_name": "Irina",
    "last_name": "Afanasieva",
    "username": "Lola",
    "password": "qwe"
}
```