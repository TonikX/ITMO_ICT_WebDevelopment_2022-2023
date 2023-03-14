# Get specific warrior
Выводит информацию о конкретном войне, его профессии и умениях.

## Information

**URL:** `/war/warrior/<int:pk>/`

**Method:** `GET`

**AUTH required:** NO

**Permissions required:** None

**Data constraints:** `{}`

## Success Responses

**Code:** `200 OK`

**Content:** `{[]}`
``` python
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
}
```