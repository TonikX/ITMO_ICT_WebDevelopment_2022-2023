**Данная конечная точка выводит список всех расписаний и информацию о них.**

**URL**: `/schedule/`

**Method**: `GET`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Code**: `200 OK`

**Content**: `{[]}`

`Ниже представлен неполный пример вывода:`

``` json
[
    {
        "id": 1,
        "show_breed": "Корги/Corgi",
        "show_time": "2020-07-20T12:00:00Z",
        "ring_number": 1,
        "show_class": "Open",
        "show_schedule": 1
    },
    {
        "id": 2,
        "show_breed": "Самоед/Samoyed",
        "show_time": "2020-07-20T13:00:00Z",
        "ring_number": 2,
        "show_class": "Open",
        "show_schedule": 1
    }
]
```