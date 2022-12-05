**Данная конечная точка позволяет просмотреть подробную информацию о конкретном эксперте, изменить её (одно поле или несколько) и удалить при необходимости.**

**URL**: `/expert/{id}/`

**Methods**: `GET, PUT, PATCH, DELETE`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Parameters**: `id` — идентификатор нужного эксперта

**Code GET**: `200 OK`

**Code PUT**: `200 OK`

**Code PATCH**: `200 OK`

**Code DELETE**: `204 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода для GET:`

``` json
{
    "id": 1,
    "expert_surname": "Samoedkin",
    "expert_name": "Andrey",
    "expert_patronymic": "Pavlovich",
    "expert_passport": "4018280459",
    "expert_phone_number": "89214098477",
    "expert_email": "apsamoedkin@gmail.com",
    "club": 1
}
```

`Ниже представлен пример вывода для PUT (вместо <string> необходимо вписать нужные строковые значения, вместо <integer> — нужные целочисленные значения):`

``` json
{
  "expert_surname": "<string>",
  "expert_name": "<string>",
  "expert_patronymic": "<string>",
  "expert_passport": "<string>",
  "expert_phone_number": "<string>",
  "expert_email": "<string>",
  "club": <integer>
}
```

**Необходимо учесть, что вводимые в поле "club" значения должны существовать в таблице "Club".**

`Ниже представлен пример вывода для PATCH (вместо <string> необходимо вписать нужные строковые значения, вместо <integer> — нужные целочисленные значения):`

``` json
{
  "expert_surname": "<string>",
  "expert_name": "<string>",
  "expert_patronymic": "<string>",
  "expert_passport": "<string>",
  "expert_phone_number": "<string>",
  "expert_email": "<string>",
  "club": <integer>
}
```

**Необходимо учесть, что вводимые в поле "club" значения должны существовать в таблице "Club".**