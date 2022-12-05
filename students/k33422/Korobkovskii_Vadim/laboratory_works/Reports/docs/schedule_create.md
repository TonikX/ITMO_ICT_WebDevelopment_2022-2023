**Данная конечная точка позволяет внести в систему новое расписание и информацию о нем.**

**URL**: `/schedule/create`

**Method**: `POST`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Code**: `201 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода (вместо <integer> необходимо вписать нужные целочисленные значения, вместо <datetime> — дату и время, вместо <choice> — выбрать один из вариантов, предложенных в выпадающем списке):`

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