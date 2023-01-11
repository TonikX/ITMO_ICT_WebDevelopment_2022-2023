**Данная конечная точка позволяет просмотреть подробную информацию о конкретной собаке, изменить её (одно поле или несколько) и удалить при необходимости.**

**URL**: `/club/{id}/`

**Methods**: `GET, PUT, PATCH, DELETE`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Parameters**: `id` — идентификатор нужной собаки

**Code GET**: `200 OK`

**Code PUT**: `200 OK`

**Code PATCH**: `200 OK`

**Code DELETE**: `204 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода для GET:`

``` json
{
    "id": 1,
    "dog_name": "Fluffy",
    "breed": "Корги/Corgi",
    "full_age": 2,
    "month_age": 24,
    "dog_class": "Show",
    "document": "1",
    "dad_name": "Waddles",
    "mom_name": "Queeny",
    "last_vaccination": "2022-10-25",
    "dog_info": "",
    "dog_owner": 1,
    "dog_club": 1
}
```

`Ниже представлен пример вывода для PUT (вместо <string> необходимо вписать нужные строковые значения, вместо <integer> — нужные целочисленные значения, вместо <date> — дату, вместо <choice> — выбрать один из вариантов, предложенных в выпадающем списке):`

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

`Ниже представлен пример вывода для PATCH (вместо <string> необходимо вписать нужные строковые значения, вместо <integer> — нужные целочисленные значения, вместо <date> — дату, вместо <choice> — выбрать один из вариантов, предложенных в выпадающем списке):`

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
