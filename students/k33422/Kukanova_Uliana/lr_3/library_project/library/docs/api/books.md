# Показать все книги

Выводит информацию о всех книгах

**URL** : `/books/list/`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
   "Books": [
    {
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
]
}
```