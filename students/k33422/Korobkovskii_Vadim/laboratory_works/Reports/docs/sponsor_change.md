**Данная конечная точка позволяет просмотреть подробную информацию о конкретном споносоре, изменить её (одно поле или несколько) и удалить при необходимости.**

**URL**: `/expert/{id}/`

**Methods**: `GET, PUT, PATCH, DELETE`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Parameters**: `id` — идентификатор нужного спонсора

**Code GET**: `200 OK`

**Code PUT**: `200 OK`

**Code PATCH**: `200 OK`

**Code DELETE**: `204 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода для GET:`

``` json
{
    "id": 1,
    "sponsor_name": "Everything for our little friends",
    "sponsor_phone_number": "89325409147",
    "sponsor_email": "everythingforfriends@gmail.com"
}
```

`Ниже представлен пример вывода для PUT (вместо <string> необходимо вписать нужные строковые значения):`

``` json
{
  "sponsor_name": "string",
  "sponsor_phone_number": "string",
  "sponsor_email": "string"
}
```
`Ниже представлен пример вывода для PATCH (вместо <string> необходимо вписать нужные строковые значения):`

``` json
{
  "sponsor_name": "string",
  "sponsor_phone_number": "string",
  "sponsor_email": "string"
}
```