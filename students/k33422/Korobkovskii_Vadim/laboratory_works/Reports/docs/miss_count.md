**Данная конечная точка выводит список количество собак, которые были не допущены или были сняты с определенной выставки.**

**URL**: `/miss_count/{id}`

**Method**: `GET`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Parameters**: `id` — идентификатор нужной выставки

**Code**: `200 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода:`

``` json
{
    "counter": 1,
    "dogs": [
        {
            "show_dog__name": "Doggy Show",
            "show_dog__begin_date": "2020-07-20T12:00:00Z",
            "participant_dog__breed": "Пудель/Poodle",
            "participant_dog__dog_name": "Storm"
        }
    ]
}
```