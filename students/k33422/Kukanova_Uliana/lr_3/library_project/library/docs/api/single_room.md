# Вывести зал по id, изменить информацию о нём, удалить его

Выводит информацию об одном зале по id, изменяет данные о нём и удаляет его

**URL** : `/rooms/<int:pk>/`

**Methods** : `GET, PATCH, DELETE`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{}`

```json
{
   "Room": {
    "id": 1,
    "books": [
        "Шерлок Холмс"
    ],
    "name": "Малый 1",
    "capacity": 30
}
}
```