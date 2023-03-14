# Show breed counts

Shows how many dogs of each breed there is

**URL** : `/breeds_count/`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{}`

```json
{
    "breed_count": [
        {
            "breed": "p",
            "count": 1
        },
        {
            "breed": "r",
            "count": 3
        }
    ]
}```
