**Данная конечная точка позволяет внести в систему нового зарегистрированного эксперта и информацию о регистрации.**

**URL**: `/expert_reg/create`

**Method**: `POST`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Code**: `201 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода (вместо <integer> необходимо вписать нужные целочисленные значения, вместо <date> — дату, вместо <choice> — выбрать один из вариантов, предложенных в выпадающем списке):`

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