**Данная конечная точка выводит список пород и количество собак, которые её представляют.**

**URL**: `/breeds_count/`

**Method**: `GET`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Code**: `200 OK`

**Content**: `{[]}`

`Ниже представлен вывод:`

``` json
{
    "breed_counter": [
        {
            "breed": "Бигль/Beagle",
            "count": 1
        },
        {
            "breed": "Доберман/Doberman",
            "count": 1
        },
        {
            "breed": "Корги/Corgi",
            "count": 3
        },
        {
            "breed": "Немецкая овчарка/German shepherd",
            "count": 3
        },
        {
            "breed": "Пудель/Poodle",
            "count": 1
        },
        {
            "breed": "Ретривер/Retriever",
            "count": 3
        },
        {
            "breed": "Самоед/Samoyed",
            "count": 3
        }
    ]
}
```