**Данная конечная точка позволяет просмотреть подробную информацию о конкретном владельце собак, изменить её (одно поле или несколько) и удалить при необходимости.**

**URL**: `/owner/{id}/`

**Methods**: `GET, PUT, PATCH, DELETE`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Parameters**: `id` — идентификатор нужного владельца собаки

**Code GET**: `200 OK`

**Code PUT**: `200 OK`

**Code PATCH**: `200 OK`

**Code DELETE**: `204 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода для GET:`

``` json
{
    "id": 1,
    "owner_surname": "Pozdnyakov",
    "owner_name": "Alexey",
    "owner_patronymic": "Ivanovich",
    "owner_passport": "4012255100",
    "owner_phone_number": "89119116939",
    "owner_email": "alex-pozd51@gmail.com"
}
```

`Ниже представлен пример вывода для PUT (вместо <string> необходимо вписать нужные строковые значения):`

``` json
{
    "owner_surname": "<string>",
    "owner_name": "<string>",
    "owner_patronymic": "<string>",
    "owner_passport": "<string>",
    "owner_phone_number": "<string>",
    "owner_email": "<string>"
}
```
`Ниже представлен пример вывода для PATCH (вместо <string> необходимо вписать нужные строковые значения):`

``` json
{
    "owner_surname": "<string>",
    "owner_name": "<string>",
    "owner_patronymic": "<string>",
    "owner_passport": "<string>",
    "owner_phone_number": "<string>",
    "owner_email": "<string>"
}
```
