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
        "breed": "b",
        "experts": []
    },
    {
        "breed": "t",
        "experts": [
            {
                "id": 2,
                "name": "Dlloy",
                "last_name": "Cate",
                "club": "Tigers"
            }
        ]
    }
]
```
