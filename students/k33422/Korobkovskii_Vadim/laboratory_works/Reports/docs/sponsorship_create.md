**Данная конечная точка позволяет внести в систему новое спонсорство и информацию о нем.**

**URL**: `/sponsorship/create`

**Method**: `POST`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Code**: `201 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода (вместо <integer> необходимо вписать нужные целочисленные значения, вместо <date> — дату, вместо <choice> — выбрать один из вариантов, предложенных в выпадающем списке):`

``` json
{
  "contract_number": <integer>,
  "sign_date": "<date>",
  "sponsor": <integer>,
  "sponsor_show": <integer>
}
```

**Необходимо учесть, что вводимые в поля "sponsor" и "sponsor_show" значения должны существовать в таблицах "Sponsor" и "Show" соответственно.** 