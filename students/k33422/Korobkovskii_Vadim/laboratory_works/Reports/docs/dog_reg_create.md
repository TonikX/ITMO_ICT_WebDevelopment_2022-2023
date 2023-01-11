**Данная конечная точка позволяет внести в систему новую зарегистрированную собаку и информацию о регистрации.**

**URL**: `/dog_reg/create`

**Method**: `POST`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Code**: `201 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода (вместо <string> необходимо вписать нужные строковые значения, вместо <integer> — нужные целочисленные значения, вместо <date> — дату, вместо <choice> — выбрать один из вариантов, предложенных в выпадающем списке):`

``` json
{
  "show_dog_number": <integer>,
  "dog_status": "<choice>",
  "reg_dog_date": "<date>",
  "bill": "<choice>",
  "checkup": "<choice>",
  "checkup_date": "<date>",
  "show_medal": "<choice>",
  "participant_dog": <integer>,
  "show_dog": <integer>
}
```

**Необходимо учесть, что вводимые в поля "participant_dog" и "show_dog" значения должны существовать в таблицах "Dog" и "Show" соответственно.** 