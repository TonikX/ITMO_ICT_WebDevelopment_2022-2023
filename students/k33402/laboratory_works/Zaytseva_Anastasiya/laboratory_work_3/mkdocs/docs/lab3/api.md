# Показать все книги

Выводит информацию обо всех книгах

**URL** : `/api/v1/book`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : NO

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "id": 1,
        "title": "Введение в реляционные базы данных",
        "isbn": 9785941577705,
        "page_count": 464,
        "price": 777,
        "has_illustrations": true,
        "book_category": 1
    },
    {
        "id": 2,
        "title": "Код. Тайный язык информатики",
        "isbn": 9780735605053,
        "page_count": 393,
        "price": 1299,
        "has_illustrations": false,
        "book_category": 5
    },
    {
        "id": 3,
        "title": "Полный справочник по C++, 4-е издание",
        "isbn": 9785845904898,
        "page_count": 800,
        "price": 999,
        "has_illustrations": false,
        "book_category": 2
    }
]
```