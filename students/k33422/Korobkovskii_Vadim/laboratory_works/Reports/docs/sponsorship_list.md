**Данная конечная точка выводит список всех спонсорств и информацию о них.**

**URL**: `/sponsorship/`

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
        "contract_number": 1,
        "sign_date": "2020-09-01",
        "sponsor": 1,
        "sponsor_show": 2
    },
    {
        "id": 2,
        "contract_number": 2,
        "sign_date": "2021-09-01",
        "sponsor": 1,
        "sponsor_show": 5
    }
]
```