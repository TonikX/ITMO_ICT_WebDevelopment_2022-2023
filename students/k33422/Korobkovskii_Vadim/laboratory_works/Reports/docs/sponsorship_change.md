**Данная конечная точка позволяет просмотреть подробную информацию о конкретном спонсорстве, изменить её (одно поле или несколько) и удалить при необходимости.**

**URL**: `/sponsorship/{id}/`

**Methods**: `GET, PUT, PATCH, DELETE`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Parameters**: `id` — идентификатор нужного спонсорства

**Code GET**: `200 OK`

**Code PUT**: `200 OK`

**Code PATCH**: `200 OK`

**Code DELETE**: `204 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода для GET:`

``` json
{
    "id": 1,
    "contract_number": 1,
    "sign_date": "2020-09-01",
    "sponsor": 1,
    "sponsor_show": 2
}
```

`Ниже представлен пример вывода для PUT (вместо <integer> необходимо вписать нужные целочисленные значения, вместо <date> — дату, вместо <choice> — выбрать один из вариантов, предложенных в выпадающем списке):`

``` json
{
  "contract_number": <integer>,
  "sign_date": "<date>",
  "sponsor": <integer>,
  "sponsor_show": <integer>
}
```

**Необходимо учесть, что вводимые в поля "sponsor" и "sponsor_show" значения должны существовать в таблицах "Sponsor" и "Show" соответственно.** 

`Ниже представлен пример вывода для PATCH (вместо <integer> необходимо вписать нужные целочисленные значения, вместо <date> — дату, вместо <choice> — выбрать один из вариантов, предложенных в выпадающем списке):`

``` json
{
  "contract_number": <integer>,
  "sign_date": "<date>",
  "sponsor": <integer>,
  "sponsor_show": <integer>
}
```

**Необходимо учесть, что вводимые в поля "sponsor" и "sponsor_show" значения должны существовать в таблицах "Sponsor" и "Show" соответственно.** 