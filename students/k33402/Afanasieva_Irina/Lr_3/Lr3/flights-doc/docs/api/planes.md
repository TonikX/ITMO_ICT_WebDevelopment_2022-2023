## Самолеты - endpoints

### Список самолетов

**URL** : `planes/all`

**Method** : `GET`

**Code** : `200 OK`

**Content** : `{[]}`

```json
     {
        "id": 1,
        "company": "S7",
        "model": "Airbus320",
        "prod_date": "2022-02-24"
    },
    {
        "id": 2,
        "company": "S7",
        "model": "Airbus380",
        "prod_date": "2022-01-24"
    },
    {
        "id": 3,
        "company": "S7",
        "model": "Boeing 737-500",
        "prod_date": "2010-02-24"
    },
    {
        "id": 4,
        "company": "S7",
        "model": "Boeing 767",
        "prod_date": "2012-02-24"
    }
```

### Добавление нового судна

**URL** : `planes/create/`

**Method** : `POST`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
     "company": null,
     "model": "",
     "prod_date": "null"
}
```

### Редактирование (get/update/delete) информации о существующем судне

**URL** : `planes/<int:pk>/`

**Method** : `GET`, `PUT`, `PATCH`, `DELETE`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "company": "S7",
    "model": "Boeing 767",
    "prod_date": "2012-02-24"
}
```