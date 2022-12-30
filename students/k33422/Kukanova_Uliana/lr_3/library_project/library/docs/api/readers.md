# Показать всех читателей

Выводит информацию обо всех читателях

**URL** : `/readers/list/`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
   "Readers": [
    {
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
]
}
```