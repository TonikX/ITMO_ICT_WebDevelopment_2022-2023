# Показать библиотеку

Выводит информацию о библиотеке

**URL** : `/library/list/`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
   "Library": [
    {
        "id": 1,
        "room": [
            "Малый 1",
            "Большой 1"
        ],
        "name": "Главная библиотека"
    }
]
}
```