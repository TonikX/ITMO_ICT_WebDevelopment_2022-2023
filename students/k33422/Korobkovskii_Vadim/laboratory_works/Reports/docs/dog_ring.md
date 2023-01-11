**Данная конечная точка выводит список выставок и рингов, на которых выступали все собаки определенного хозяина.**

**URL**: `/dog_ring/{id}`

**Method**: `GET`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Parameters**: `id` — идентификатор нужного хозяина

**Code**: `200 OK`

**Content**: `{[]}`

`Ниже представлен неполный пример вывода:`

``` json
{
    "rings": [
        {
            "schedule_grade__show_schedule__name": "Doggy Show",
            "schedule_grade__show_schedule__begin_date": "2020-07-20T12:00:00Z",
            "dog_grade__participant_dog__dog_name": "Fluffy",
            "dog_grade__participant_dog__breed": "Корги/Corgi",
            "schedule_grade__ring_number": 1
        },
        {
            "schedule_grade__show_schedule__name": "Big Corgy",
            "schedule_grade__show_schedule__begin_date": "2020-09-12T13:00:00Z",
            "dog_grade__participant_dog__dog_name": "Fluffy",
            "dog_grade__participant_dog__breed": "Корги/Corgi",
            "schedule_grade__ring_number": 1
        }
    ]
}
```