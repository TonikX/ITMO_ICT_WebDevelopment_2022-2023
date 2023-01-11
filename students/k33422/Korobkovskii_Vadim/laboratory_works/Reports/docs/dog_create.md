**Данная конечная точка позволяет внести в систему новыю собаку и информацию о ней.**

**URL**: `/dog/create`

**Method**: `POST`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Code**: `201 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода (вместо <string> необходимо вписать нужные строковые значения, вместо <integer> — нужные целочисленные значения, вместо <date> — дату, вместо <choice> — выбрать один из вариантов, предложенных в выпадающем списке):`

``` json
{
  "dog_name": "<string>",
  "breed": "<choice>",
  "full_age": <integer>,
  "month_age": <integer>,
  "dog_class": "<choice>",
  "document": "<string>",
  "dad_name": "<string>",
  "mom_name": "<string>",
  "last_vaccination": "<date>",
  "dog_info": "<string>",
  "dog_owner": <integer>,
  "dog_club": <integer>
}
```

**Необходимо учесть, что вводимые в поля "dog_owner" и "dog_club" значения должны существовать в таблицах "Owner" и "Club" соответственно.** 