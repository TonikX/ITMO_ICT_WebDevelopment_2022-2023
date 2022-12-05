**Данная конечная точка выводит список всех выставок и информацию о них.**

**URL**: `/show/`

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
        "name": "Doggy Show",
        "begin_date": "2020-07-20T12:00:00Z",
        "end_date": "2020-07-20T18:00:00Z",
        "city": "Saint-Petersburg",
        "address": "Tipanova street, 7",
        "show_type": "Поли/Poly",
        "host": 1
    },
    {
        "id": 2,
        "name": "Big Corgy",
        "begin_date": "2020-09-12T13:00:00Z",
        "end_date": "2020-07-20T16:00:00Z",
        "city": "Saint-Petersburg",
        "address": "Nevskiy avenue , 120",
        "show_type": "Моно/Mono",
        "host": 1
    }
]
```