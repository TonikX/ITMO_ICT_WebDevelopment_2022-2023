**Данная конечная точка выводит список всех экспертов и информацию о них.**

**URL**: `/expert/`

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
        "expert_surname": "Samoedkin",
        "expert_name": "Andrey",
        "expert_patronymic": "Pavlovich",
        "expert_passport": "4018280459",
        "expert_phone_number": "89214098477",
        "expert_email": "apsamoedkin@gmail.com",
        "club": 1
    },
    {
        "id": 2,
        "expert_surname": "Dogov",
        "expert_name": "Sergey",
        "expert_patronymic": "Viktorovich",
        "expert_passport": "4016850120",
        "expert_phone_number": "89119246508",
        "expert_email": "dogov@mail.ru",
        "club": 1
    }
]
```