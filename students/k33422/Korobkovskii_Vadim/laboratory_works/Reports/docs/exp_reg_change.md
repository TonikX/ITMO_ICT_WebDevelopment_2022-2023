**Данная конечная точка позволяет просмотреть подробную информацию о конкретном зарегистрированном эксперте, изменить её (одно поле или несколько) и удалить при необходимости.**

**URL**: `/expert_reg/{id}/`

**Methods**: `GET, PUT, PATCH, DELETE`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Parameters**: `id` — идентификатор нужного зарегистрированного эксперта

**Code GET**: `200 OK`

**Code PUT**: `200 OK`

**Code PATCH**: `200 OK`

**Code DELETE**: `204 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода для GET:`

``` json
{
    "id": 68,
    "show_exp_number": 2,
    "exp_status": "Участвовал/Participated",
    "reg_exp_date": "2020-07-13",
    "participant_exp": 5,
    "show_exp": 1
}
```

`Ниже представлен пример вывода для PUT (вместо <integer> необходимо вписать нужные целочисленные значения, вместо <date> — дату, вместо <choice> — выбрать один из вариантов, предложенных в выпадающем списке):`

``` json
{
  "show_exp_number": <integer>,
  "exp_status": "<choice>",
  "reg_exp_date": "<date>",
  "participant_exp": <integer>,
  "show_exp": <integer>
}
```

**Необходимо учесть, что вводимые в поля "participant_exp" и "show_exp" значения должны существовать в таблицах "Expert" и "Show" соответственно.** 

`Ниже представлен пример вывода для PATCH (вместо <integer> необходимо вписать нужные целочисленные значения, вместо <date> — дату, вместо <choice> — выбрать один из вариантов, предложенных в выпадающем списке):`

``` json
{
  "show_exp_number": <integer>,
  "exp_status": "<choice>",
  "reg_exp_date": "<date>",
  "participant_exp": <integer>,
  "show_exp": <integer>
}
```

**Необходимо учесть, что вводимые в поля "participant_exp" и "show_exp" значения должны существовать в таблицах "Expert" и "Show" соответственно.** 