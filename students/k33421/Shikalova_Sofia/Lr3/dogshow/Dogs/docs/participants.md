# Show, delete and replace a participant

Shows info about a participant

**URL** : `/participants/<id>`

**Method** : `GET PUT PATCH`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{}`

```json
{
    "id": 1,
    "name": "Rex",
    "breed": "r",
    "age": 5,
    "family": "Rex's parents",
    "vaccinated": "2021-11-30",
    "owner_data": "Owner",
    "dismissed": false,
    "club": null,
    "rings": [
        1,
        1
    ],
    "medals": [
        1
    ]
}```
