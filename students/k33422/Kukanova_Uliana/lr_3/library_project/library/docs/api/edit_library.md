# Изменить информацию о библиотеке, удалить её

Изменяет данные о библиотеке и удаляет её

**URL** : `/library/<int:pk>/`

**Methods** : `GET, PATCH, DELETE`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{}`

```json
{
   "Library": {
    "id": 1,
    "room": [
        "Малый 1",
        "Большой 1"
    ],
    "name": "Главная библиотека"
}
}
```