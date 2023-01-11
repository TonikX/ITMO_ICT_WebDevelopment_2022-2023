**Данная конечная точка позволяет внести в систему нового эксперта и информацию о нем.**

**URL**: `/expert/create`

**Method**: `POST`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Code**: `201 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода (вместо <string> необходимо вписать нужные строковые значения, вместо <integer> — нужные целочисленные значения):`

``` json
{
  "expert_surname": "<string>",
  "expert_name": "<string>",
  "expert_patronymic": "<string>",
  "expert_passport": "<string>",
  "expert_phone_number": "<string>",
  "expert_email": "<string>",
  "club": <integer>
}
```

**Необходимо учесть, что вводимые в поле "club" значения должны существовать в таблице "Club".** 