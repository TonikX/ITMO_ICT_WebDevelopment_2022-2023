# Показать всех воинов

**URL** : `/api/warriors/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
   "Warriors": [
       {
           "id": 1,
           "race": "t",
           "name": "Petr2",
           "level": 0,
           "profession": null,
           "skill": []
       },
       {
           "id": 2,
           "race": "t",
           "name": "Petr",
           "level": 0,
           "profession": null,
           "skill": []
       }
   ]
}
```