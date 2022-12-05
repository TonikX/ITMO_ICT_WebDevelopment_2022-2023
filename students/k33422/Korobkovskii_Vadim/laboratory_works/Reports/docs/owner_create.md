**Данная конечная точка позволяет внести в систему нового владельцев собак и информацию о нем.**

**URL**: `/owner/create`

**Method**: `POST`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Code**: `201 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода (вместо <string> необходимо вписать нужные строковые значения):`

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