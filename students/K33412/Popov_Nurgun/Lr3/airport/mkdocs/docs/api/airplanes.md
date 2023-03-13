## AIRPLANE endpoints

### List of airplanes

**URL** : `airplanes/`

**Method** : `GET`

**Code** : `200 OK`

**Content** : `{[]}`

```json
    {
        "id": 1,
        "tail_number": "RP-C3224",
        "type": "Airbus",
        "seats": 150,
        "velocity": 840,
        "airline": "S7 Airlines",
        "under_maintenance": false
    },
    {
        "id": 2,
        "tail_number": "VQ-BOZ",
        "type": "Airbus",
        "seats": 150,
        "velocity": 840,
        "airline": "Nordwind Airlines",
        "under_maintenance": false
    },
    {
        "id": 3,
        "tail_number": "N468AC",
        "type": "Boeing",
        "seats": 168,
        "velocity": 807,
        "airline": "Nordwind Airlines",
        "under_maintenance": false
    },
    {
        "id": 4,
        "tail_number": "N737RD",
        "type": "Boeing",
        "seats": 168,
        "velocity": 807,
        "airline": "S7 Airlines",
        "under_maintenance": true
    }
```

### Add a new airplane

**URL** : `airplanes/create/`

**Method** : `POST`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "tail_number": "",
    "type": "",
    "seats": null,
    "velocity": null,
    "airline": "",
    "under_maintenance": false
}
```

### Modify (get/update/delete) an existing airplane

**URL** : `airplanes/<int:pk>/`

**Method** : `GET`, `PUT`, `PATCH`, `DELETE`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 1,
    "tail_number": "RP-C3224",
    "type": "Airbus",
    "seats": 150,
    "velocity": 840,
    "airline": "S7 Airlines",
    "under_maintenance": false
}
```