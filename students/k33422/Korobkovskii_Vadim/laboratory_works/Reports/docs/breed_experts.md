**Данная конечная точка выводит список всех экспертов и породы собак, которые они когда-либо судили.**

**URL**: `/breed_experts/`

**Method**: `GET`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Code**: `200 OK`

**Content**: `{[]}`

`Ниже представлен пример неполного вывода:`

``` json

{
    "breeds": [
        {
            "dog_grade__participant_dog__breed": "Бигль/Beagle",
            "expert_grade__participant_exp__expert_surname": "Pushistiy",
            "expert_grade__participant_exp__expert_name": "Vadim",
            "expert_grade__participant_exp__expert_patronymic": "Aleksandrovich"
        },
        {
            "dog_grade__participant_dog__breed": "Бигль/Beagle",
            "expert_grade__participant_exp__expert_surname": "Govorova",
            "expert_grade__participant_exp__expert_name": "Marina",
            "expert_grade__participant_exp__expert_patronymic": "Mikhailovna"
        }
    ]
}
```