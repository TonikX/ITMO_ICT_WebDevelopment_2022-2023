## TRANSIT endpoints

### List of transit destinations

**URL** : `transit/`

**Method** : `GET`

**Code** : `200 OK`

**Content** : `{[]}`

```json
     {
        "id": 1,
        "destination": "Новосибирск"
    },
    {
        "id": 2,
        "destination": "Москва"
    }
```

### Add a new transit destination

**URL** : `transit/create/`

**Method** : `POST`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "destination": ""
}
```

### Modify (get/update/delete) an existing transit destination

**URL** : `transit/<int:pk>/`

**Method** : `GET`, `PUT`, `PATCH`, `DELETE`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 1,
    "destination": "Новосибирск"
}
```