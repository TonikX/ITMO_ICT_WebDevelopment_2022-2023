# Воины

Воины с профессией, уровнем и навыками.

## Показать всех воинов

Выводит информацию обо всех войнах

**URL** : `/war/warriors/`

**Method** : `GET`

### Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "Warriors": [
        {
            "id": 1,
            "race": "s",
            "name": "Warrior1",
            "level": 1,
            "profession": 1,
            "skill": [
                1
            ]
        }
    ]
}
```
## Данные о воине

Выводит информацию о воине с возможностью обновления и удаления.

**URL** : `/war/warriors/{id}`

**Method** : `GET, PUT, PATCH, DELETE, HEAD, OPTIONS`

### Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 1,
    "skill": [
        {
            "id": 1,
            "name": "skill"
        }
    ],
    "profession": {
        "id": 1,
        "name": "profession1",
        "description": "bla bla"
    },
    "race": "s",
    "name": "Warrior1",
    "level": 1
}
```