# Get all warriors
Выводит информацию обо всех войнах, их профессиях и умениях.

## Information

**URL:** `/war/warriors/`

**Method:** `GET`

**AUTH required:** NO

**Permissions required:** None

**Data constraints:** `{}`

## Success Responses

**Code:** `200 OK`

**Content:** `{[]}`
``` python
[
    {
        "id": 1,
        "job": {
            "title": "Game Designer",
            "description": "doing some strange stuff"
        },
        "skill": [
            {
                "id": 1,
                "title": "Python"
            }
        ],
        "race": "s",
        "name": "Lev Kobelev",
        "level": 20
    },
    {
        "id": 2,
        "job": {
            "title": "Analytics",
            "description": "doing some maths stuff"
        },
        "skill": [
            {
                "id": 1,
                "title": "Python"
            }
        ],
        "race": "s",
        "name": "Kev Lobelev",
        "level": 21
    }
]
```