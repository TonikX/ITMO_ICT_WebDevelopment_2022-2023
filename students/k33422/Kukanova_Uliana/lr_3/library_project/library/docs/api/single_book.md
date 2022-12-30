# Вывести книгу по id, изменить информацию о ней, удалить её

Выводит информацию об одной книге по id, изменяет данные о ней и удаляет её

**URL** : `/books/<int:pk>/`

**Methods** : `GET, PATCH, DELETE`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{}`

```json
{
   "Book": {
    "id": 1,
    "author": {
        "name": "Артур Конан Дойль"
    },
    "publisher": {
        "name": "Bloomsbury"
    },
    "section": {
        "name": "Детектив"
    },
    "name": "Шерлок Холмс",
    "year": 2009,
    "code": "123456",
    "date": "2022-01-12T02:25:59Z"
}
}
```