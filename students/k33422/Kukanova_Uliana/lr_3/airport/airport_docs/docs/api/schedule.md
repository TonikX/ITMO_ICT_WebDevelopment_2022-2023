## SCHEDULE endpoints

### List of scheduled flights

**URL** : `schedule/`

**Method** : `GET`

**Code** : `200 OK`

**Content** : `{[]}`

```json
     {
        "number": 1010,
        "distance": 635,
        "departure": "Санкт-Петербург",
        "arrival": "Москва",
        "completed": 33,
        "transit": null
    },
    {
        "number": 5103,
        "distance": 3313,
        "departure": "Новосибирск",
        "arrival": "Сочи",
        "completed": 17,
        "transit": null
    },
    {
        "number": 6023,
        "distance": 3618,
        "departure": "Санкт-Петербург",
        "arrival": "Кемерово",
        "completed": 4,
        "transit": 2
    }
```

### Add a new scheduled flight

**URL** : `schedule/create/`

**Method** : `POST`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "number": null,
    "distance": null,
    "departure": "",
    "arrival": "",
    "completed": null,
    "transit": null
}
```

### Modify (get/update/delete) an existing scheduled flight

**URL** : `schedule/<int:pk>/`

**Method** : `GET`, `PUT`, `PATCH`, `DELETE`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
        "number": 5103,
        "distance": 3313,
        "departure": "Новосибирск",
        "arrival": "Сочи",
        "completed": 17,
        "transit": null
    }
```