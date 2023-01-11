**Данная конечная точка позволяет просмотреть подробную информацию о конкретной выставке, изменить её (одно поле или несколько) и удалить при необходимости.**

**URL**: `/club/{id}/`

**Methods**: `GET, PUT, PATCH, DELETE`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Parameters**: `id` — идентификатор нужной выставки

**Code GET**: `200 OK`

**Code PUT**: `200 OK`

**Code PATCH**: `200 OK`

**Code DELETE**: `204 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода для GET:`

``` json
{
    "id": 1,
    "name": "Doggy Show",
    "begin_date": "2020-07-20T12:00:00Z",
    "end_date": "2020-07-20T18:00:00Z",
    "city": "Saint-Petersburg",
    "address": "Tipanova street, 7",
    "show_type": "Поли/Poly",
    "host": 1
}
```

`Ниже представлен пример вывода для PUT (вместо <string> необходимо вписать нужные строковые значения, вместо <integer> — нужные целочисленные значения, вместо <datetime> — дату и время, вместо <choice> — выбрать один из вариантов, предложенных в выпадающем списке):`

``` json
{
  "name": "<string>",
  "begin_date": "<datetime>",
  "end_date": "<datetime>>",
  "city": "<string>",
  "address": "<string>",
  "show_type": "<choice>",
  "host": <integer>
}
```

**Необходимо учесть, что вводимые в поле "host" значения должны существовать в таблице "Organizer".** 

`Ниже представлен пример вывода для PATCH (вместо <string> необходимо вписать нужные строковые значения, вместо <integer> — нужные целочисленные значения, вместо <datetime> — дату и время, вместо <choice> — выбрать один из вариантов, предложенных в выпадающем списке):`

``` json
{
  "name": "<string>",
  "begin_date": "<datetime>",
  "end_date": "<datetime>>",
  "city": "<string>",
  "address": "<string>",
  "show_type": "<choice>",
  "host": <integer>
}
```

**Необходимо учесть, что вводимые в поле "host" значения должны существовать в таблице "Organizer".** 