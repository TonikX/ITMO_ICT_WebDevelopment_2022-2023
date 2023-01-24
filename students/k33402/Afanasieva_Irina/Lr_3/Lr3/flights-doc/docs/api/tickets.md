## Билеты - endpoints

### Список билетов

**URL** : `tickets/all`

**Method** : `GET`

**Code** : `200 OK`

**Content** : `{[]}`

```json
    {
        "id": 1,
        "flight": {
            "id": 1,
            "number": "689GY7",
            "departure": "2022-03-24T14:46:08Z",
            "arrival": "2022-03-24T16:46:12Z",
            "wherefrom": "Moskow",
            "whereto": "Maldives",
            "gate": "10",
            "plane": 1
        },
        "passenger": {
            "first_name": "Sonya",
            "last_name": "Marmeladova"
        },
        "number": "678Hy"
    },
    {
        "id": 2,
        "flight": {
            "id": 2,
            "number": "666HHt7",
            "departure": "2022-03-25T14:47:07Z",
            "arrival": "2022-02-26T00:47:13Z",
            "wherefrom": "Russia",
            "whereto": "Argentina",
            "gate": "8",
            "plane": 2
        },
        "passenger": {
            "first_name": "Irina",
            "last_name": "Afanasieva"
        },
        "number": "7779ngg"
    },
```

### Добавление нового билета

**URL** : `tickets/create/`

**Method** : `POST`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "number": "",
    "flight": null,
    "passenger": null
}
```

### Редактирование (get/update/delete) информации о существующем билете

**URL** : `tickets/<int:pk>/`

**Method** : `GET`, `PUT`, `PATCH`, `DELETE`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "number": "879Fhk7",
    "flight": "HYK76L, Russia -> Argentina",
    "passenger": "Lola - Irina Afanasieva"
}
```