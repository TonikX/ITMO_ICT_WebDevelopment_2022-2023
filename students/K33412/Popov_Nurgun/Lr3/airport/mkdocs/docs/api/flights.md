## FLIGHTS endpoints

### List of flights

**URL** : `flights/`

**Method** : `GET`

**Code** : `200 OK`

**Content** : `{[]}`

```json
     {
        "id": 1,
        "crew": 4,
        "tickets_sold": 356,
        "departure_date": "2023-02-16",
        "departure_time": "02:34:00",
        "arrival_date": "2023-02-17",
        "arrival_time": "17:30:00",
        "transit_arrival_date": "2023-02-16",
        "transit_arrival_time": "10:30:00",
        "transit_departure_date": "2023-02-16",
        "transit_departure_time": "16:30:00",
        "number": 1010,
        "plane_id": 1
    },
    
```

### Add a new flight

**URL** : `flights/create/`

**Method** : `POST`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "crew": null,
    "tickets_sold": null,
    "departure_date": null,
    "departure_time": null,
    "arrival_date": null,
    "arrival_time": null,
    "transit_arrival_date": null,
    "transit_arrival_time": null,
    "transit_departure_date": null,
    "transit_departure_time": null,
    "number": null,
    "plane_id": null
}
```

### Modify (get/update/delete) an existing flight

**URL** : `flights/<int:pk>/`

**Method** : `GET`, `PUT`, `PATCH`, `DELETE`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "id": 1,
    "crew": 4,
    "tickets_sold": 356,
    "departure_date": "2023-02-16",
    "departure_time": "02:34:00",
    "arrival_date": "2023-02-17",
    "arrival_time": "17:30:00",
    "transit_arrival_date": "2023-02-16",
    "transit_arrival_time": "10:30:00",
    "transit_departure_date": "2023-02-16",
    "transit_departure_time": "16:30:00",
    "number": 1010,
    "plane_id": 1
}
```