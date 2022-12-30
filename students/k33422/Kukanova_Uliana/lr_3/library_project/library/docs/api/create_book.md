# Создать книгу

Создаёт новую книгу

**URL** : `/books/create/`

**Methods** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `201 Created`

**Content** : `{}`

```json
{
   "Book": {
    "id": 2,
    "name": "Гарри Поттер",
    "year": 2010,
    "code": "176797",
    "date": "2022-01-12T05:42:00Z",
    "author": 2,
    "publisher": 1,
    "section": 1
}
}
```