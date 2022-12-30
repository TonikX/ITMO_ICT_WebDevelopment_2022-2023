# Создать читателя

Создаёт нового читателя

**URL** : `/readers/create/`

**Methods** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `201 Created`

**Content** : `{}`

```json
{
   "Reader": {
    "id": 2,
    "books": [],
    "ticket": "54321",
    "name": "Морозов Михаил Маркович",
    "passport": "4020567833",
    "birth_date": "2001-12-28",
    "address": "пр. Ленина, д. 42",
    "phone_number": "+79023457652",
    "education": "в",
    "degree": true,
    "registration_date": "2022-01-12",
    "room": 2
}
}
```