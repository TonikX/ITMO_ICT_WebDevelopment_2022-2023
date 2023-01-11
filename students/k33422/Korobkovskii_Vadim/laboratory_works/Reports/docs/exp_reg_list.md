**Данная конечная точка выводит список всех зарегистрированных на какую-либо выставку экспертов и информацию о них.**

**URL**: `/expert_reg/`

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
        "id": 67,
        "show_exp_number": 1,
        "exp_status": "Участвовал/Participated",
        "reg_exp_date": "2020-07-13",
        "participant_exp": 10,
        "show_exp": 1
    },
    {
        "id": 68,
        "show_exp_number": 2,
        "exp_status": "Участвовал/Participated",
        "reg_exp_date": "2020-07-13",
        "participant_exp": 5,
        "show_exp": 1
    }
]
```