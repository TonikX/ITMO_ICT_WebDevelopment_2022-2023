## FLIGHTS endpoints

### List of flights

**URL** : `flights/`

**Method** : `GET`

**Code** : `200 OK`

**Content** : `{[]}`

```json
     {
        "id": 1,
        "crew": 1,
        "tickets_sold": 124,
        "departure_date": "2021-12-02",
        "departure_time": "20:23:00",
        "arrival_date": "2021-12-02",
        "arrival_time": "22:01:00",
        "transit_arrival_date": null,
        "transit_arrival_time": null,
        "transit_departure_date": null,
        "transit_departure_time": null,
        "number": 1010,
        "plane_id": 1
    },
    {
        "id": 2,
        "crew": 2,
        "tickets_sold": 98,
        "departure_date": "2021-11-29",
        "departure_time": "11:20:00",
        "arrival_date": "2021-11-29",
        "arrival_time": "12:30:00",
        "transit_arrival_date": null,
        "transit_arrival_time": null,
        "transit_departure_date": null,
        "transit_departure_time": null,
        "number": 5103,
        "plane_id": 2
    }
    {
        "id": 3,
        "crew": 1,
        "tickets_sold": 162,
        "departure_date": "2021-11-30",
        "departure_time": "19:45:00",
        "arrival_date": "2021-12-01",
        "arrival_time": "07:15:00",
        "transit_arrival_date": "2021-11-30",
        "transit_arrival_time": "21:20:00",
        "transit_departure_date": "2021-11-30",
        "transit_departure_time": "22:55:00",
        "number": 6023,
        "plane_id": 3
    }
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
    "crew": 1,
    "tickets_sold": 124,
    "departure_date": "2021-12-02",
    "departure_time": "20:23:00",
    "arrival_date": "2021-12-02",
    "arrival_time": "22:01:00",
    "transit_arrival_date": null,
    "transit_arrival_time": null,
    "transit_departure_date": null,
    "transit_departure_time": null,
    "number": 1010,
    "plane_id": 1
}
```