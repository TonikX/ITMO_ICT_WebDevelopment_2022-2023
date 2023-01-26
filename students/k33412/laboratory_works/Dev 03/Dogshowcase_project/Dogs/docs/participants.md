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
    "name": "furry",
    "breed": "t",
    "age": 5,
    "family": "A-10",
    "owner_data": "12.01.22",
    "club": null
},
{
    "id": 2,
    "name": "Avatar",
    "breed": "h",
    "age": 8,
    "family": "A-11",
    "owner_data": "12.01.15",
    "club": null
}```