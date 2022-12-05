**Данная конечная точка позволяет просмотреть подробную информацию о конкретном клубе, изменить её (одно поле или несколько) и удалить при необходимости.**

**URL**: `/club/{id}/`

**Methods**: `GET, PUT, PATCH, DELETE`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Parameters**: `id` — идентификатор нужного клуба

**Code GET**: `200 OK`

**Code PUT**: `200 OK`

**Code PATCH**: `200 OK`

**Code DELETE**: `204 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода для GET:`

``` json
{
    "id": 1,
    "name": "For dog bones!",
    "club_phone_number": "89211008888",
    "club_email": "fordogbones@gmail.com"
}
```

`Ниже представлен пример вывода для PUT (вместо <string> необходимо вписать нужные значения):`

``` json
{
    "name": "<string>",
    "club_phone_number": "<string>",
    "club_email": "<string>",
}
```
`Ниже представлен пример вывода для PATCH (вместо <string> необходимо вписать нужные строковые значения):`

``` json
{
    "name": "<string>",
    "club_phone_number": "<string>",
    "club_email": "<string>",
}
```
