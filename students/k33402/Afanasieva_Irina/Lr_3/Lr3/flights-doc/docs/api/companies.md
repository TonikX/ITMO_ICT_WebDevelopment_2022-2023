## Авиакомпании - endpoints

### Список компаний

**URL** : `airlines/all`

**Method** : `GET`

**Code** : `200 OK`

**Content** : `{[]}`

```json
      {
        "id": 1,
        "name": "S7",
        "owner": "Burger King",
        "phone": "8988666553"
    },
    {
        "id": 2,
        "name": "Emirates",
        "owner": "Papa",
        "phone": "6988656553"
    }
```

### Добавление новой компании

**URL** : `airlines/create/`

**Method** : `POST`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "name": "",
    "owner": "",
    "phone": ""
}
```

### Редактирование (get/update/delete) информации о существующей компании

**URL** : `airlines/<int:pk>/`

**Method** : `GET`, `PUT`, `PATCH`, `DELETE`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "name": "S7",
    "owner": "Burger King",
    "phone": "6988656553"
}
```