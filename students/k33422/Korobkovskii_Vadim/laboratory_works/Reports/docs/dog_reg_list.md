**Данная конечная точка выводит список всех зарегистрированных на какую-либо выставку собак и информацию о них.**

**URL**: `/dog_reg/`

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
        "show_dog_number": 1,
        "dog_status": "Участвовал/Participated",
        "reg_dog_date": "2020-07-15",
        "bill": "Оплачен/Paid",
        "checkup": "Пройден/Passed",
        "checkup_date": "2020-07-18",
        "show_medal": null,
        "participant_dog": 1,
        "show_dog": 1
    },
    {
        "id": 2,
        "show_dog_number": 2,
        "dog_status": "Участвовал/Participated",
        "reg_dog_date": "2020-07-13",
        "bill": "Оплачен/Paid",
        "checkup": "Пройден/Passed",
        "checkup_date": "2020-07-15",
        "show_medal": null,
        "participant_dog": 7,
        "show_dog": 1
    }
]
```