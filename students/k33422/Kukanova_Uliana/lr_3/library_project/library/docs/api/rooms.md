# Показать залы

Выводит информацию о всех залах

**URL** : `/rooms/list/`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
   "Rooms": [
    {
        "id": 1,
        "books": [
            "Шерлок Холмс"
        ],
        "name": "Малый 1",
        "capacity": 30
    },
    {
        "id": 2,
        "books": [],
        "name": "Большой 1",
        "capacity": 60
    }
]
}
```