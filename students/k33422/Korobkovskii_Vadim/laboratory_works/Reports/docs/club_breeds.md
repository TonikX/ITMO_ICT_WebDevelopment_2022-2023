**Данная конечная точка выводит список все породы собак, которыми представлен определенный клуб.**

**URL**: `/club_breeds/{id}`

**Method**: `GET`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Parameters**: `id` — идентификатор нужного клуба

**Code**: `200 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода:`

``` json
{
    "breeds": [
        {
            "breed": "Доберман/Doberman",
            "count": 1
        },
        {
            "breed": "Корги/Corgi",
            "count": 1
        },
        {
            "breed": "Самоед/Samoyed",
            "count": 1
        }
    ]
}
```