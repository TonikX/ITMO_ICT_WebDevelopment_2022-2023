**Данная конечная точка выводит список всех спонсоров и информацию о них.**

**URL**: `/sponsor/`

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
        "sponsor_name": "Everything for our little friends",
        "sponsor_phone_number": "89325409147",
        "sponsor_email": "everythingforfriends@gmail.com"
    },
    {
        "id": 2,
        "sponsor_name": "Money for dogs",
        "sponsor_phone_number": "89319245029",
        "sponsor_email": "moneyfordogs@gmail.com"
    }
]
```