**Данная конечная точка позволяет внести в систему новые оценки.**

**URL**: `/grading/create`

**Method**: `POST`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Code**: `201 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода (вместо <integer> необходимо вписать нужные целочисленные значения):`

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

**Поле sum заполнять не надо, оно заполнится автоматически на основе введеных в поля "grade1", "grade2" и "grade3" значения.**