**Данная конечная точка позволяет внести в систему новую выставку и информацию о ней.**

**URL**: `/show/create`

**Method**: `POST`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Code**: `201 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода (вместо <string> необходимо вписать нужные строковые значения, вместо <integer> — нужные целочисленные значения, вместо <datetime> — дату и время, вместо <choice> — выбрать один из вариантов, предложенных в выпадающем списке):`

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