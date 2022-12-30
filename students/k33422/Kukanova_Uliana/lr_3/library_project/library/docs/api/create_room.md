# Создать зал

Создаёт новый зал

**URL** : `/rooms/create/`

**Methods** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `201 Created`

**Content** : `{}`

```json
{
   "Room": {
    "id": 3,
    "books": [],
    "name": "Малый 2",
    "capacity": 20
}
}
```