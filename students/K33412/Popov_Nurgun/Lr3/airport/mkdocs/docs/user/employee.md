## EMPLOYEE endpoints

### List of employees
**URL** : `employees/`

**Method** : `GET`

**Code** : `200 OK`

**Content** : `{[]}`

```json
    {
        "passport": "8042759234",
        "full_name": "Коняева Надежда Михайловна",
        "age": 46,
        "education": "ВО",
        "experience": 22,
        "in_crew": 1
    },
    {
        "passport": "8085927461",
        "full_name": "Рожков Вадим Артемович",
        "age": 32,
        "education": "СПО",
        "experience": 9,
        "in_crew": 2
    }
```

### Add a new employee
**URL** : `employees/create/`

**Method** : `POST`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "passport": "",
    "full_name": "",
    "age": null,
    "education": null,
    "experience": null,
    "in_crew": null
}
```

### Modify (get/update/delete) an existing employee
**URL** : `employees/<int:pk>/`

**Method** : `GET`, `PUT`, `PATCH`, `DELETE`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "passport": "8042759234",
    "full_name": "Коняева Надежда Михайловна",
    "age": 46,
    "education": "ВО",
    "experience": 22,
    "in_crew": 1
}
```