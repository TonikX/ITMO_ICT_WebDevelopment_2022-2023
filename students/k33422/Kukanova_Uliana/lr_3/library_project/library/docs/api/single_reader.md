# Вывести пользователя по id, изменить информацию о нём, удалить его

Выводит информацию об одном пользователе по id, изменяет данные о нём и удаляет его

**URL** : `/readers/<int:pk>/`

**Methods** : `GET, PATCH, DELETE`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{}`

```json
{
   "Reader": {
    "id": 1,
    "books": [
        "Шерлок Холмс"
    ],
    "ticket": "12345",
    "name": "Иванов Иван Иванович",
    "passport": "4020567832",
    "birth_date": "2022-01-12",
    "address": "ул. Мира, д.52",
    "phone_number": "+79023457651",
    "education": "с",
    "degree": false,
    "registration_date": "2022-01-12",
    "room": 1
}
}
```