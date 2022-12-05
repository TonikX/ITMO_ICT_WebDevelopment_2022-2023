**Данная конечная точка выводит список всех владельцев собак и информацию о них.**

**URL**: `/owner/`

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
        "owner_surname": "Pozdnyakov",
        "owner_name": "Alexey",
        "owner_patronymic": "Ivanovich",
        "owner_passport": "4012255100",
        "owner_phone_number": "89119116939",
        "owner_email": "alex-pozd51@gmail.com"
    },
    {
        "id": 2,
        "owner_surname": "Bolshakova",
        "owner_name": "Elena",
        "owner_patronymic": "Ivanovna",
        "owner_passport": "4012512940",
        "owner_phone_number": "89123409281",
        "owner_email": "elenab@gmail.com"
    }
]
```