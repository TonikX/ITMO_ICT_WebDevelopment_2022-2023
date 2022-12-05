**Данная конечная точка позволяет внести в систему нового спонсора и информацию о нем.**

**URL**: `/sponsor/create`

**Method**: `POST`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Code**: `201 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода (вместо <string> необходимо вписать нужные строковые значения):`

``` json
{
  "sponsor_name": "string",
  "sponsor_phone_number": "string",
  "sponsor_email": "string"
}
```