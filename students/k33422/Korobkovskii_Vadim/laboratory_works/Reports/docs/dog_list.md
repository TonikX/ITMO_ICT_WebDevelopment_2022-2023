**Данная конечная точка выводит список всех собак и информацию о них.**

**URL**: `/dog/`

**Method**: `GET`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Code**: `200 OK`

**Content**: `{[]}`

`Ниже представлен неполный пример вывода:`

``` json
[
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
    },
    {
        "id": 2,
        "dog_name": "Cloudy",
        "breed": "Самоед/Samoyed",
        "full_age": 1,
        "month_age": 16,
        "dog_class": "Show",
        "document": "2",
        "dad_name": "King",
        "mom_name": "Ameliya",
        "last_vaccination": "2022-10-25",
        "dog_info": "",
        "dog_owner": 1,
        "dog_club": 1
    }
]
```