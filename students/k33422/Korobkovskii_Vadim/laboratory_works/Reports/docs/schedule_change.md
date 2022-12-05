**Данная конечная точка позволяет просмотреть подробную информацию о конкретном расписании, изменить её (одно поле или несколько) и удалить при необходимости.**

**URL**: `/schedule/{id}/`

**Methods**: `GET, PUT, PATCH, DELETE`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Parameters**: `id` — идентификатор нужного расписания

**Code GET**: `200 OK`

**Code PUT**: `200 OK`

**Code PATCH**: `200 OK`

**Code DELETE**: `204 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода для GET:`

``` json
{
    "id": 1,
    "show_breed": "Корги/Corgi",
    "show_time": "2020-07-20T12:00:00Z",
    "ring_number": 1,
    "show_class": "Open",
    "show_schedule": 1
}
```

`Ниже представлен пример вывода для PUT (вместо <integer> необходимо вписать нужные целочисленные значения, вместо <datetime> — дату и время, вместо <choice> — выбрать один из вариантов, предложенных в выпадающем списке):`

``` json
{
  "show_breed": "<choice>",
  "show_time": "<datetime>",
  "ring_number": <integer>,
  "show_class": "<choice>",
  "show_schedule": <integer>
}
```

**Необходимо учесть, что вводимые в поле "show_schedule" значения должны существовать в таблице "Show".** 

`Ниже представлен пример вывода для PATCH (вместо <integer> необходимо вписать нужные целочисленные значения, вместо <datetime> — дату и время, вместо <choice> — выбрать один из вариантов, предложенных в выпадающем списке):`

``` json
{
  "show_breed": "<choice>",
  "show_time": "<datetime>",
  "ring_number": <integer>,
  "show_class": "<choice>",
  "show_schedule": <integer>
}
```

**Необходимо учесть, что вводимые в поле "show_schedule" значения должны существовать в таблице "Show".**  