**Данная конечная точка выводит список всех оценок и информацию о них.**

**URL**: `/grading/`

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
        "grade1": 6,
        "grade2": 7,
        "grade3": 6,
        "sum": 19,
        "schedule_grade": 1,
        "dog_grade": 1,
        "expert_grade": 67
    },
    {
        "id": 2,
        "grade1": 8,
        "grade2": 8,
        "grade3": 6,
        "sum": 22,
        "schedule_grade": 1,
        "dog_grade": 3,
        "expert_grade": 67
    }
]
```