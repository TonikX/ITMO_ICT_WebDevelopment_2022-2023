**Данная конечная точка позволяет просмотреть подробную информацию о конкретной зарегистрированной собаке, изменить её (одно поле или несколько) и удалить при необходимости.**

**URL**: `/club/{id}/`

**Methods**: `GET, PUT, PATCH, DELETE`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Parameters**: `id` — идентификатор нужной зарегистрированной собаки

**Code GET**: `200 OK`

**Code PUT**: `200 OK`

**Code PATCH**: `200 OK`

**Code DELETE**: `204 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода для GET:`

``` json
{
    "id": 1,
    "show_dog_number": 1,
    "dog_status": "Участвовал/Participated",
    "reg_dog_date": "2020-07-15",
    "bill": "Оплачен/Paid",
    "checkup": "Пройден/Passed",
    "checkup_date": "2020-07-18",
    "show_medal": null,
    "participant_dog": 1,
    "show_dog": 1
}
```

`Ниже представлен пример вывода для PUT (вместо <string> необходимо вписать нужные строковые значения, вместо <integer> — нужные целочисленные значения, вместо <date> — дату, вместо <choice> — выбрать один из вариантов, предложенных в выпадающем списке):`

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

`Ниже представлен пример вывода для PATCH (вместо <string> необходимо вписать нужные строковые значения, вместо <integer> — нужные целочисленные значения, вместо <date> — дату, вместо <choice> — выбрать один из вариантов, предложенных в выпадающем списке):`

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