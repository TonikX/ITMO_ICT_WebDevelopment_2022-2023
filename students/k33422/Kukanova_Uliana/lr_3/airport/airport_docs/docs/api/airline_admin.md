## AIRLINE ADMINISTRATION endpoints

### List of employees and their jobs

**URL** : `airline_admin/`

**Method** : `GET`

**Code** : `200 OK`

**Content** : `{[]}`

```json
      {
        "id": 1,
        "job": "штурман",
        "clearance": true,
        "employee": 1
    },
    {
        "id": 2,
        "job": "второй пилот",
        "clearance": true,
        "employee": 2
    }
```

### Assign a job to an employee

**URL** : `airline_admin/create/`

**Method** : `POST`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "job": "",
    "clearance": false,
    "employee": null
}
```

### Modify (get/update/delete) an existing arrangement

**URL** : `airline_admin/<int:pk>/`

**Method** : `GET`, `PUT`, `PATCH`, `DELETE`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 1,
    "job": "штурман",
    "clearance": true,
    "employee": 1
}
```