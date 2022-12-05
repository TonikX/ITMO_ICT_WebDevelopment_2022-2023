**Данная конечная точка позволяет просмотреть подробную информацию об оценках, изменить её (одно поле или несколько) и удалить при необходимости.**

**URL**: `/grading/{id}/`

**Methods**: `GET, PUT, PATCH, DELETE`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Parameters**: `id` — идентификатор нужного оценивания

**Code GET**: `200 OK`

**Code PUT**: `200 OK`

**Code PATCH**: `200 OK`

**Code DELETE**: `204 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода для GET:`

``` json
{
    "id": 1,
    "grade1": 6,
    "grade2": 7,
    "grade3": 6,
    "sum": 19,
    "schedule_grade": 1,
    "dog_grade": 1,
    "expert_grade": 67
}
```

`Ниже представлен пример вывода для PUT (вместо <integer> необходимо вписать нужные целочисленные значения):`

``` json
{
  "grade1": <integer>,
  "grade2": <integer>,
  "grade3": <integer>,
  "sum": <integer>,
  "schedule_grade": <integer>,
  "dog_grade": <integer>,
  "expert_grade": <integer>
}
```

**Необходимо учесть, что вводимые в поля "schedule_grade", "dog_grade" и "expert_grade" значения должны существовать в таблицах "ShowSchedule", "DogParticipation" и "ExpertParticipation".** 

`Ниже представлен пример вывода для PATCH (вместо <integer> необходимо вписать нужные целочисленные значения):`

``` json
{
  "grade1": <integer>,
  "grade2": <integer>,
  "grade3": <integer>,
  "sum": <integer>,
  "schedule_grade": <integer>,
  "dog_grade": <integer>,
  "expert_grade": <integer>
}
```

**Необходимо учесть, что вводимые в поля "schedule_grade", "dog_grade" и "expert_grade" значения должны существовать в таблицах "ShowSchedule", "DogParticipation" и "ExpertParticipation".** 