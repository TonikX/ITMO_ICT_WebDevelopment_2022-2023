# Shows info about which breeds are judged by an expert

Shows info about which breeds are judged by an expert

**URL** : `/breed_experts/`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `[]`

```json
[
    {
        "breed": "r",
        "experts": [
            {
                "id": 1,
                "name": "Juan",
                "last_name": "Andreev",
                "club": "Hunt",
                "ring": null
            },
            {
                "id": 2,
                "name": "Anton",
                "last_name": "Antonov",
                "club": "Hunt",
                "ring": 1
            }
        ]
    }
]
```
