**Данная конечная точка позволяет внести в систему новый клуб и информацию о нем.**

**URL**: `/club/create`

**Method**: `POST`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Code**: `201 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода (вместо <string> необходимо вписать нужные строковые значения):`

``` json
{
    "name": "<string>",
    "club_phone_number": "<string>",
    "club_email": "<string>",
}
```