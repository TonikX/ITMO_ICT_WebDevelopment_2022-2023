## Рейсы - endpoints

### Список рейсов

**URL** : `flights/all`

**Method** : `GET`

**Code** : `200 OK`

**Content** : `{[]}`

```json
    {
        "id": 1,
        "plane": "Airbus320",
        "number": "689GY7",
        "departure": "2022-03-24T14:46:08Z",
        "arrival": "2022-03-24T16:46:12Z",
        "wherefrom": "Russia",
        "whereto": "Maldives",
        "gate": "10"
    },
    {
        "id": 2,
        "plane": "Airbus380",
        "number": "666HHt7",
        "departure": "2022-03-25T14:47:07Z",
        "arrival": "2022-02-26T00:47:13Z",
        "wherefrom": "Russia",
        "whereto": "Argentina",
        "gate": "8"
    },
```

### Добавление нового рейса

**URL** : `flights/create/`

**Method** : `POST`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "plane": null,
    "number": "",
    "departure": null,
    "arrival": null,
    "wherefrom": "",
    "whereto": "",
    "gate": ""
}
```

### Редактирование (get/update/delete) информации о существующем рейсе

**URL** : `flights/<int:pk>/`

**Method** : `GET`, `PUT`, `PATCH`, `DELETE`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "plane": "Boeing 767",
    "number": "77Ia45",
    "departure": "2022-02-28T14:48:37Z",
    "arrival": "2022-02-28T16:48:14Z",
    "wherefrom": "Russia",
    "whereto": "Maldives",
    "gate": "6"
}
```