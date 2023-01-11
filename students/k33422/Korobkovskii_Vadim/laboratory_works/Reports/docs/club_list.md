**Данная конечная точка выводит список всех клубов и информацию о них.**

**URL**: `/club/`

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
        "name": "For dog bones!",
        "club_phone_number": "89211008888",
        "club_email": "fordogbones@gmail.com"
    },
    {
        "id": 2,
        "name": "Fuzzy tail",
        "club_phone_number": "89118604204",
        "club_email": "fuzzytail@yandex.ru"
    }
]
```