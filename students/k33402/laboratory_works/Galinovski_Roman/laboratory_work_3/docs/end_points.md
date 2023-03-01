**Таблица для хранения данных о зарегистрированных пользователях, организаторов выставок.**
 
`Таблица имеет следующие поля:`
  1. "surname" хранит фамилию организатора
  2. "name" хранит имя организатора
  3. "patronymic" хранит отчество организатора
  4. "phone_number" хранит номер телефона организатора
  5. "passport" хранит серию и номер пасспорта организатора
  6. "mail" хранит эл.почту
   
**Таблица для хранения данных о клубах.**
 
`Таблица имеет следующие поля:`
  1. Поле "name" хранит название клуба
  2. Поле "phone_number" хранит номер телефона клуба
  3. Поле "email" хранит почтовый адрес клуба 

**End-point выводит список все породы собак определенного клуба.**

**URL**: `/club_breeds/{id}`

**Method**: `GET`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Parameters**: `id` — ID Клуба

**Code**: `200 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода:`

``` json
{
    "breeds": [
        {
            "breed": "Achihuahua",
            "count": 1
        },
        {
            "breed": "Sobaka",
            "count": 1
        },
        {
            "breed": "Ovcharka",
            "count": 1
        }
    ]
}
```
**End-point позволяет просмотреть подробную информацию о конкретном клубе, изменить её (одно поле или несколько) и удалить при необходимости.**

**URL**: `/club/{id}/`

**Methods**: `GET, PUT, PATCH, DELETE`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Parameters**: `id` — ID клуба

**Code GET**: `200 OK`

**Code PUT**: `200 OK`

**Code PATCH**: `200 OK`

**Code DELETE**: `204 OK`

**Content**: `{[]}`

`Пример вывода для GET:`

``` json
{
    "id": 1,
    "name": "dog's boner!",
    "phone_number": "89999999999",
    "email": "dogboner@yandex.ru"
}
```

`Пример вывода для PUT (<string> - нужные значения):`

``` json
{
    "name": "<string>",
    "phone_number": "<string>",
    "email": "<string>",
}
```
`Пример вывода для PATCH ( <string> - нужные строковые значения):`

``` json
{
    "name": "<string>",
    "phone_number": "<string>",
    "email": "<string>",
}
```
**End-point позволяет внести в систему новый клуб и информацию о нем.**

**URL**: `/club/create`

**Method**: `POST`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Code**: `201 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода ( <string> - нужные строковые значения):`

``` json
{
    "name": "<string>",
    "club_phone_number": "<string>",
    "club_email": "<string>",
}
```
**End-point выводит список всех клубов и информацию о них.**

**URL**: `/club/`

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
        "name": "For dog bones!",
        "club_phone_number": "89211008888",
        "club_email": "fordogbones@gmail.com"
    },
    {
        "id": 2,
        "name": "fairytails",
        "club_phone_number": "88918604305",
        "club_email": "fairytails@yandex.ru"
    }
]
```
**Таблица для хранения данных о владельцах собак.**

`Таблица имеет следующие поля:`
  1. "surname" хранит фамилию владельца
  2. "name" хранит имя владельца
  3. "patronymic" хранит отчество владельца
  4. "phone_number" хранит номер телефона владельца
  5. "passport" хранит серию и номер пасспорта владельца
  6. "email" хранит почтовый адрес владельца
   
**End-point позволяет просмотреть подробную информацию о конкретном владельце собак, изменить её (одно поле или несколько) и удалить при необходимости.**

**URL**: `/owner/{id}/`

**Methods**: `GET, PUT, PATCH, DELETE`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Parameters**: `id` — ID Владельца

**Code GET**: `200 OK`

**Code PUT**: `200 OK`

**Code PATCH**: `200 OK`

**Code DELETE**: `204 OK`

**Content**: `{[]}`

`Пример вывода для GET:`
``` json
{
    "id": 1,
    "owner_surname": "Mavashi",
    "owner_name": "Misha",
    "owner_patronymic": "IVan",
    "owner_passport": "40336275190",
    "owner_phone_number": "89222222222",
    "owner_email": "momashevashei62@gmail.com"
}
```

`Пример вывода для PUT (<string> - нужные строковые значения):`
``` json
{
    "owner_surname": "<string>",
    "owner_name": "<string>",
    "owner_patronymic": "<string>",
    "owner_passport": "<string>",
    "owner_phone_number": "<string>",
    "owner_email": "<string>"
}
```
`Пример вывода для PATCH (<string> - нужные строковые значения):`
``` json
{
    "owner_surname": "<string>",
    "owner_name": "<string>",
    "owner_patronymic": "<string>",
    "owner_passport": "<string>",
    "owner_phone_number": "<string>",
    "owner_email": "<string>"
}
```
**End-point позволяет внести в систему нового владельцев собак и информацию о нем.**

**URL**: `/owner/create`

**Method**: `POST`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Code**: `201 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода (вместо <string> необходимо вписать нужные строковые значения):`

``` json
{
    "owner_surname": "<string>",
    "owner_name": "<string>",
    "owner_patronymic": "<string>",
    "owner_passport": "<string>",
    "owner_phone_number": "<string>",
    "owner_email": "<string>"
}
```
**End-point выводит список всех владельцев собак и информацию о них.**

**URL**: `/owner/`

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
        "owner_surname": "Mavashi",
        "owner_name": "Misha",
        "owner_patronymic": "IVan",
        "owner_passport": "40336275190",
        "owner_phone_number": "89222222222",
        "owner_email": "momashevashei62@gmail.com"
    },
    {
        "id": 2,
        "owner_surname": "Menshikov",
        "owner_name": "Igor",
        "owner_patronymic": "Igorevich",
        "owner_passport": "40126275190",
        "owner_phone_number": "89333333333",
        "owner_email": "igoreb@gmail.com"
    }
]
```
**Таблица для хранения данных о собаках.**
 
`Таблица имеет следующие поля:`

  1. "name" хранит кличку собаки
  2. "breed" хранит породу собаки, которую надо выбрать из списка
  3. "full_age" хранит возраст собаки в годах
  4. "month_age" хранит возраст собаки в месяцах
  5. "classof_dog" хранит классность собаки, которую надо выбрать из списка   
  6. "document" хранит номер документа о породистости собаки
  7. "last_vaccination" хранит дату последней вакцинации собаки
  8.  "owner" является внешним ключом к таблице Owner
  9.  "club" является внешним ключом к таблице Club
   
**End-point позволяет просмотреть подробную информацию о конкретной собаке, изменить её и удалить при необходимости.**

**URL**: `/club/{id}/`

**Methods**: `GET, PUT, PATCH, DELETE`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Parameters**: `id` — ID Собаки

**Code GET**: `200 OK`

**Code PUT**: `200 OK`

**Code PATCH**: `200 OK`

**Code DELETE**: `204 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода для GET:`

``` json
{
    "id": 1,
    "name": "god",
    "breed": "Sobaka",
    "full_age": 4,
    "month_age": 48,
    "classof_dog": "Show",
    "document": "1337",
    "last_vaccination": "2023-01-25",
    "owner": 1,
    "club": 1
}
```

`Ниже представлен пример вывода для PUT (вместо <string> необходимо вписать нужные строковые значения, вместо <integer> — нужные целочисленные значения, вместо <date> — дату, вместо <choice> — выбрать один из вариантов, предложенных в выпадающем списке):`

``` json
{
  "name": "<string>",
  "breed": "<choice>",
  "full_age": <integer>,
  "month_age": <integer>,
  "classof_dog": "<choice>",
  "document": "<string>",
  "last_vaccination": "<date>",
  "owner": <integer>,
  "club": <integer>
}
```
**Вводимые в поля "owner" и "club" значения должны существовать в таблицах "Owner" и "Club" соответственно.** 

`Ниже представлен пример вывода для PATCH (<string> - нужные строковые значения, <integer> — нужные целочисленные значения, <date> — дату, <choice> — выбрать один из вариантов, предложенных в выпадающем списке):`

``` json
{
  "name": "<string>",
  "breed": "<choice>",
  "full_age": <integer>,
  "month_age": <integer>,
  "classof_dog": "<choice>",
  "document": "<string>",
  "last_vaccination": "<date>",
  "owner": <integer>,
  "club": <integer>
}
```
**End-point позволяет внести в систему новыю собаку и информацию о ней.**

**URL**: `/dog/create`

**Method**: `POST`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Code**: `201 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода (<string> - нужные строковые значения, <integer> — нужные целочисленные значения, <date> — дату, <choice> — выбрать один из вариантов, предложенных в выпадающем списке):`

``` json
{
  "name": "<string>",
  "breed": "<choice>",
  "full_age": <integer>,
  "month_age": <integer>,
  "classof_dog": "<choice>",
  "document": "<string>",
  "last_vaccination": "<date>",
  "owner": <integer>,
  "club": <integer>
}
```
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
        "name": "god",
        "breed": "Sobaka",
        "full_age": 4,
        "month_age": 48,
        "classof_dog": "Show",
        "document": "1337",
        "last_vaccination": "2023-01-25",
        "owner": 1,
        "club": 1
    },
    {
        "id": 2,
        "name": "doggy",
        "breed": "Sobaka",
        "full_age": 4,
        "month_age": 48,
        "classof_dog": "Show",
        "document": "1339",
        "last_vaccination": "2023-01-25",
        "owner": 1,
        "club": 1
    }
]
```
**Таблица для хранения данных о выставках.**
 
`Таблица имеет следующие поля:`
  1.  "name" хранит название выставки
  2.  "dateof_begin" хранит дату и время начала выставки
  3.  "dateof_end" хранит дату и время окончания выставки
  4.  "city" хранит город, в котором пройдем выставка
  5.  "address" хранит адрес, по которому пройдет выставка
  6.  "typeof_show" хранит тип выставки, который надо выбрать из списка
  7. "host" является внешним ключом к таблице Organizer

## Списки для выбора:

### Cписок для поля "show_type"

``` python
types = (
        ("Mono", "Monobreed exhibition"),
        ("Poly", "Polybreed exhibition")
)
```
**End-point позволяет просмотреть подробную информацию о конкретной выставке, изменить её (одно поле или несколько) и удалить при необходимости.**

**URL**: `/club/{id}/`

**Methods**: `GET, PUT, PATCH, DELETE`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Parameters**: `id` — идентификатор нужной выставки

**Code GET**: `200 OK`

**Code PUT**: `200 OK`

**Code PATCH**: `200 OK`

**Code DELETE**: `204 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода для GET:`

``` json
{
    "id": 1,
    "name": "Dog show",
    "dateof_begin": "2023-01-20T12:00:00Z",
    "dateof_end": "2023-01-20T18:00:00Z",
    "city": "Saint-Petersburg",
    "address": "Titova street, 7",
    "show_type": "Poly",
    "host": 1
}
```

`Ниже представлен пример вывода для PUT (<string> - нужные строковые значения, <integer> —  целочисленные значения, <datetime> — дату и время, <choice> — один из вариантов, предложенных в выпадающем списке):`

``` json
{
  "name": "<string>",
  "dateof_begin": "<datetime>",
  "dateof_end": "<datetime>>",
  "city": "<string>",
  "address": "<string>",
  "show_type": "<choice>",
  "host": <integer>
}
```

`Ниже представлен пример вывода для PATCH (<string> - нужные строковые значения, <integer> — целочисленные значения, <datetime> — дату и время, <choice> — один из вариантов, предложенных в выпадающем списке):`

``` json
{
  "name": "<string>",
  "dateof_begin": "<datetime>",
  "dateof_end": "<datetime>>",
  "city": "<string>",
  "address": "<string>",
  "show_type": "<choice>",
  "host": <integer>
}
```
**End-point позволяет внести в систему новую выставку и информацию о ней.**

**URL**: `/show/create`

**Method**: `POST`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Code**: `201 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода ( <string> необходимо вписать нужные строковые значения,  <integer> — нужные целочисленные значения, вместо <datetime> — дату и время, вместо <choice> — выбрать один из вариантов, предложенных в выпадающем списке):`

``` json
{
  "name": "<string>",
  "dateof_begin": "<datetime>",
  "dateof_end": "<datetime>>",
  "city": "<string>",
  "address": "<string>",
  "show_type": "<choice>",
  "host": <integer>
}
```
**End-point выводит список всех выставок и информацию о них.**

**URL**: `/show/`

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
        "name": "Dog show",
        "dateof_begin": "2023-01-20T12:00:00Z",
        "dateof_end": "2023-01-20T18:00:00Z",
        "city": "Saint-Petersburg",
        "address": "Titova street, 7",
        "show_type": "Poly",
        "host": 1
    },
    {
        "id": 2,
        "name": "God show",
        "dateof_begin": "2023-01-21T12:00:00Z",
        "dateof_end": "2023-01-21T18:00:00Z",
        "city": "Saint-Petersburg",
        "address": "Popova street, 7",
        "show_type": "Mono",
        "host": 1
    }
]
```
**Таблица для хранения данных о зарегистрированных собаках.**
 
`Таблица имеет следующие поля:`
  1.  "show_dog_number" хранит порядковый номер собаки на выставке
  2.  "status" хранит статус собаки, который надо выбрать из списка
  3.  "dateof_reg_dog" хранит дату регистрации собаки
  4.  "bill" хранит статус счёта, который надо выбрать из списка
  5.  "checkup" хранит статус медосмотра, который надо выбрать из списка    
  6.  "dateof_checkup" хранит дату медосмотра
  7.  "participant_dog" является внешним ключом к таблице Dog
  8.  "show_dog" является внешним ключом к таблице Show
  9.  "show_medal" хранит полученную на выставке (или не полученную) медаль, которую надо выбрать из списка 

## Списки для выбора:

### Cписок для поля "status"

``` python
status_choices = (
        ("Participated", "Participated"),
        ("Suspended", "Suspended"),
        ("Not allowed", "Not allowed"),
        ("Absence", "Absence")
)
```
### Cписок для поля "bill"

``` python
bill_choices = (
        ("Paid", "Paid"),
        ("Not paid", "Not paid")
)
```
### Cписок для поля "checkup"

``` python
checkup_choices = (
        ("Passed", "Medical examination was successfully passed"),
        ("Not passed", "Medical examination was not passed")
)
```
### Cписок для поля "show_medal"

``` python
medals = (
        ("Gold", "Gold for first place"),
        ("Silver", "Silver for second place"),
        ("Bronze", "Bronze for third place"),
        ("Audience award", "Medal as audience sympathy prize")
)
```
**End-point позволяет просмотреть подробную информацию о конкретной зарегистрированной собаке, изменить её (одно поле или несколько) и удалить при необходимости.**

**URL**: `/club/{id}/`

**Methods**: `GET, PUT, PATCH, DELETE`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Parameters**: `id` — ID зарегистрированной собаки

**Code GET**: `200 OK`

**Code PUT**: `200 OK`

**Code PATCH**: `200 OK`

**Code DELETE**: `204 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода для GET:`

``` json
{
    "id": 1,
    "show_dog_number": 1,
    "status": "Participated",
    "dateof_reg_dog": "2022-12-15",
    "bill": "Paid",
    "checkup": "Passed",
    "dateof_checkup": "2022-12-18",
    "show_medal": null,
    "participant_dog": 1,
    "show_dog": 1
}
```

`Ниже представлен пример вывода для PUT (вместо <string> необходимо вписать нужные строковые значения, вместо <integer> — нужные целочисленные значения, вместо <date> — дату, вместо <choice> — выбрать один из вариантов, предложенных в выпадающем списке):`

``` json
{
  "show_dog_number": <integer>,
  "status": "<choice>",
  "dateof_reg_dog": "<date>",
  "bill": "<choice>",
  "checkup": "<choice>",
  "dateof_checkup": "<date>",
  "show_medal": "<choice>",
  "participant_dog": <integer>,
  "show_dog": <integer>
}
```

`Ниже представлен пример вывода для PATCH (вместо <string> необходимо вписать нужные строковые значения, вместо <integer> — нужные целочисленные значения, вместо <date> — дату, вместо <choice> — выбрать один из вариантов, предложенных в выпадающем списке):`

``` json
{
  "show_dog_number": <integer>,
  "status": "<choice>",
  "dateof_reg_dog": "<date>",
  "bill": "<choice>",
  "checkup": "<choice>",
  "dateof_checkup": "<date>",
  "show_medal": "<choice>",
  "participant_dog": <integer>,
  "show_dog": <integer>
}
```
**End-point позволяет внести в систему новую зарегистрированную собаку и информацию о регистрации.**

**URL**: `/dog_reg/create`

**Method**: `POST`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Code**: `201 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода (вместо <string> необходимо вписать нужные строковые значения, вместо <integer> — нужные целочисленные значения, вместо <date> — дату, вместо <choice> — выбрать один из вариантов, предложенных в выпадающем списке):`

``` json
{
  "show_dog_number": <integer>,
  "status": "<choice>",
  "dateof_reg_dog": "<date>",
  "bill": "<choice>",
  "checkup": "<choice>",
  "dateof_checkup": "<date>",
  "show_medal": "<choice>",
  "participant_dog": <integer>,
  "show_dog": <integer>
}
```
**End-point выводит список всех зарегистрированных на какую-либо выставку собак и информацию о них.**

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
        "status": "Participated",
        "dateof_reg_dog": "2022-12-15",
        "bill": "Paid",
        "checkup": "Passed",
        "dateof_checkup": "2022-12-18",
        "show_medal": null,
        "participant_dog": 1,
        "show_dog": 1
    },
    {
        "id": 2,
        "show_dog_number": 2,
        "status": "Participated",
        "dateof_reg_dog": "2022-12-15",
        "bill": "Paid",
        "checkup": "Passed",
        "dateof_checkup": "2022-12-18",
        "show_medal": null,
        "participant_dog": 7,
        "show_dog": 1
    }
]
```
**Таблица для хранения данных об экспертах.**
 
`Таблица имеет следующие поля:`

  1.  "surname" хранит фамилию эксперта
  2.  "name" хранит имя эксперта
  3.  "patronymic" хранит отчество эксперта
  4.  "phone_number" хранит номер телефона эксперта
  5.  "passport" хранит серию и номер пасспорта эксперта
  6. "email" хранит почтовый адрес эксперта
  7. "club" является внешним ключом к таблице Club

**End-point позволяет просмотреть подробную информацию о конкретном эксперте, изменить её (одно поле или несколько) и удалить при необходимости.**

**URL**: `/expert/{id}/`

**Methods**: `GET, PUT, PATCH, DELETE`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Parameters**: `id` — ID эксперта

**Code GET**: `200 OK`

**Code PUT**: `200 OK`

**Code PATCH**: `200 OK`

**Code DELETE**: `204 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода для GET:`

``` json
{
    "id": 1,
    "surname": "Alyushin",
    "name": "Valera",
    "patronymic": "Pavlovich",
    "passport": "1234567890",
    "phone_number": "892112345678",
    "email": "jijakeen@gmail.com",
    "club": 1
}
```

`Ниже представлен пример вывода для PUT (вместо <string> необходимо вписать нужные строковые значения, вместо <integer> — нужные целочисленные значения):`

``` json
{
  "surname": "<string>",
  "name": "<string>",
  "patronymic": "<string>",
  "passport": "<string>",
  "phone_number": "<string>",
  "email": "<string>",
  "club": <integer>
}
```

`Ниже представлен пример вывода для PATCH (вместо <string> необходимо вписать нужные строковые значения, вместо <integer> — нужные целочисленные значения):`

``` json
{
  "surname": "<string>",
  "name": "<string>",
  "patronymic": "<string>",
  "passport": "<string>",
  "phone_number": "<string>",
  "email": "<string>",
  "club": <integer>
}
```
**End-point позволяет внести в систему нового эксперта и информацию о нем.**

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
  "surname": "<string>",
  "name": "<string>",
  "patronymic": "<string>",
  "passport": "<string>",
  "phone_number": "<string>",
  "email": "<string>",
  "club": <integer>
}
```
**End-point выводит список всех экспертов и информацию о них.**

**URL**: `/expert/`

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
        "surname": "Alyushin",
        "name": "Valera",
        "patronymic": "Pavlovich",
        "passport": "1234567890",
        "phone_number": "892112345678",
        "email": "jijakeen@gmail.com",
        "club": 1
    },
    {
        "id": 2,
        "surname": "Samoev",
        "name": "Soslan",
        "patronymic": "Tigranovich",
        "passport": "0987654321",
        "phone_number": "892187654321",
        "email": "kilakill@gmail.com",
        "club": 1
    }
]
```
**Таблица для хранения данных о зарегистрированных экспертах.**
 
`Таблица имеет следующие поля:`
  1.  "number" хранит порядковый номер эксперта на выставке
  2.  "status" хранит статус эксперта, который надо выбрать из списка
  3.  "dateof_reg_exp" хранит дату регистрации эксперта
  4. "participant_exp" является внешним ключом к таблице Expert
  5.  "show_exp" является внешним ключом к таблице Show

**End-point позволяет просмотреть подробную информацию о конкретном зарегистрированном эксперте, изменить её (одно поле или несколько) и удалить при необходимости.**

**URL**: `/expert_reg/{id}/`

**Methods**: `GET, PUT, PATCH, DELETE`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Parameters**: `id` — ID зарегистрированного эксперта

**Code GET**: `200 OK`

**Code PUT**: `200 OK`

**Code PATCH**: `200 OK`

**Code DELETE**: `204 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода для GET:`

``` json
{
    "id": 68,
    "number": 2,
    "status": "Participated",
    "dateof_reg_exp": "2022-12-18",
    "participant_exp": 5,
    "show_exp": 1
}
```

`Ниже представлен пример вывода для PUT (вместо <integer> необходимо вписать нужные целочисленные значения, вместо <date> — дату, вместо <choice> — выбрать один из вариантов, предложенных в выпадающем списке):`

``` json
{
  "number": <integer>,
  "status": "<choice>",
  "dateof_reg_exp": "<date>",
  "participant_exp": <integer>,
  "show_exp": <integer>
}
```

`Ниже представлен пример вывода для PATCH (вместо <integer> необходимо вписать нужные целочисленные значения, вместо <date> — дату, вместо <choice> — выбрать один из вариантов, предложенных в выпадающем списке):`

``` json
{
  "number": <integer>,
  "status": "<choice>",
  "dateof_reg_exp": "<date>",
  "participant_exp": <integer>,
  "show_exp": <integer>
}
```
**End-point позволяет внести в систему нового зарегистрированного эксперта и информацию о регистрации.**

**URL**: `/expert_reg/create`

**Method**: `POST`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Code**: `201 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода (вместо <integer> необходимо вписать нужные целочисленные значения, вместо <date> — дату, вместо <choice> — выбрать один из вариантов, предложенных в выпадающем списке):`

``` json
{
  "number": <integer>,
  "status": "<choice>",
  "dateof_reg_exp": "<date>",
  "participant_exp": <integer>,
  "show_exp": <integer>
}
```
**End-point выводит список всех зарегистрированных на какую-либо выставку экспертов и информацию о них.**

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
        "id": 68,
        "number": 2,
        "status": "Participated",
        "dateof_reg_exp": "2022-12-18",
        "participant_exp": 5,
        "show_exp": 1
    },
    {
        "id": 68,
        "number": 2,
        "status": "Participated",
        "dateof_reg_exp": "2020-07-13",
        "participant_exp": 5,
        "show_exp": 1
    }
]
```
**Таблица для хранения данных о спонсорах.**
 
`Таблица имеет следующие поля:`

  1.  "name" хранит название спонсора
  2.  "phone_number" хранит номер телефона спонсора
  3.  "email" хранит почтовый адрес спонсора
**End-point позволяет просмотреть подробную информацию о конкретном споносоре, изменить её (одно поле или несколько) и удалить при необходимости.**

**URL**: `/expert/{id}/`

**Methods**: `GET, PUT, PATCH, DELETE`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Parameters**: `id` — ID спонсора

**Code GET**: `200 OK`

**Code PUT**: `200 OK`

**Code PATCH**: `200 OK`

**Code DELETE**: `204 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода для GET:`

``` json
{
    "id": 1,
    "name": "Prodvijenie",
    "phone_number": "89325409147",
    "email": "prodvijenie@gmail.com"
}
```

`Ниже представлен пример вывода для PUT (вместо <string> необходимо вписать нужные строковые значения):`

``` json
{
  "name": "string",
  "phone_number": "string",
  "email": "string"
}
```
`Ниже представлен пример вывода для PATCH (вместо <string> необходимо вписать нужные строковые значения):`

``` json
{
  "name": "string",
  "phone_number": "string",
  "email": "string"
}
```
**End-point позволяет внести в систему нового спонсора и информацию о нем.**

**URL**: `/sponsor/create`

**Method**: `POST`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Code**: `201 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода (вместо <string> необходимо вписать нужные строковые значения):`

``` json
{
  "name": "string",
  "phone_number": "string",
  "email": "string"
}
```
**End-point выводит список всех спонсоров и информацию о них.**

**URL**: `/sponsor/`

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
        "name": "Prodvijenie",
        "phone_number": "89325409147",
        "email": "prodvijenie@gmail.com"
    },
    {
        "id": 2,
        "name": "moneylead",
        "phone_number": "89325409147",
        "email": "moneylead@gmail.com"
    }
]
```
**Таблица для хранения данных о спонсорах.**
 
`Таблица имеет следующие поля:`
  1.  "contract_number" хранит номер контракта
  2.  "dateof_sign" хранит дату подписания контракта
  3.  "sponsor" является внешним ключом к таблице Sponsor
  4.  "sponsor_show" является внешним ключом к таблице Show
**End-point позволяет просмотреть подробную информацию о конкретном спонсорстве, изменить её (одно поле или несколько) и удалить при необходимости.**

**URL**: `/sponsorship/{id}/`

**Methods**: `GET, PUT, PATCH, DELETE`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Parameters**: `id` — идентификатор нужного спонсорства

**Code GET**: `200 OK`

**Code PUT**: `200 OK`

**Code PATCH**: `200 OK`

**Code DELETE**: `204 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода для GET:`

``` json
{
    "id": 1,
    "contract_number": 1,
    "sign_date": "2022-11-11",
    "sponsor": 1,
    "sponsor_show": 2
}
```

`Ниже представлен пример вывода для PUT (вместо <integer> необходимо вписать нужные целочисленные значения, вместо <date> — дату, вместо <choice> — выбрать один из вариантов, предложенных в выпадающем списке):`

``` json
{
  "contract_number": <integer>,
  "sign_date": "<date>",
  "sponsor": <integer>,
  "sponsor_show": <integer>
}
```

`Ниже представлен пример вывода для PATCH (вместо <integer> необходимо вписать нужные целочисленные значения, вместо <date> — дату, вместо <choice> — выбрать один из вариантов, предложенных в выпадающем списке):`

``` json
{
  "contract_number": <integer>,
  "sign_date": "<date>",
  "sponsor": <integer>,
  "sponsor_show": <integer>
}
```
**End-point позволяет внести в систему новое спонсорство и информацию о нем.**

**URL**: `/sponsorship/create`

**Method**: `POST`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Code**: `201 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода (вместо <integer> необходимо вписать нужные целочисленные значения, вместо <date> — дату, вместо <choice> — выбрать один из вариантов, предложенных в выпадающем списке):`

``` json
{
  "contract_number": <integer>,
  "sign_date": "<date>",
  "sponsor": <integer>,
  "sponsor_show": <integer>
}
```
**End-point выводит список всех спонсорств и информацию о них.**

**URL**: `/sponsorship/`

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
        "contract_number": 1,
        "sign_date": "2022-11-11",
        "sponsor": 1,
        "sponsor_show": 2
    },
    {
        "id": 2,
        "contract_number": 2,
        "sign_date": "2022-11-09",
        "sponsor": 1,
        "sponsor_show": 5
    }
]
```
**Таблица для хранения данных о расписании на выставках.**
 
`Таблица имеет следующие поля:`

  1.  "breedof_show" хранит выступающую на ринге породу, которую надо выбрать из списка
  2.  "timeof_show" хранит дату и время начала выступления на ринге
  3.  "numberof_ring" хранит номер ринга
  4.  "show_class" хранит возрастной класс выступающих на ринге собак, который надо выбрать из списка
  5.  "show_schedule" является внешним ключом к таблице Show

**End-point позволяет просмотреть подробную информацию о конкретном расписании, изменить её (одно поле или несколько) и удалить при необходимости.**

**URL**: `/schedule/{id}/`

**Methods**: `GET, PUT, PATCH, DELETE`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Parameters**: `id` — ID расписания

**Code GET**: `200 OK`

**Code PUT**: `200 OK`

**Code PATCH**: `200 OK`

**Code DELETE**: `204 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода для GET:`

``` json
{
    "id": 1,
    "breedof_show": "Sobaka",
    "timeof_show": "2022-01-20T12:00:00Z",
    "numberof_ring": 1,
    "show_class": "Open",
    "show_schedule": 1
}
```

`Ниже представлен пример вывода для PUT (вместо <integer> необходимо вписать нужные целочисленные значения, вместо <datetime> — дату и время, вместо <choice> — выбрать один из вариантов, предложенных в выпадающем списке):`

``` json
{
  "breedof_show": "<choice>",
  "timeof_show": "<datetime>",
  "numberof_ring": <integer>,
  "show_class": "<choice>",
  "show_schedule": <integer>
}
```


`Ниже представлен пример вывода для PATCH (вместо <integer> необходимо вписать нужные целочисленные значения, вместо <datetime> — дату и время, вместо <choice> — выбрать один из вариантов, предложенных в выпадающем списке):`

``` json
{
  "breedof_show": "<choice>",
  "timeof_show": "<datetime>",
  "numberof_ring": <integer>,
  "show_class": "<choice>",
  "show_schedule": <integer>
}
```
**End-point позволяет внести в систему новое расписание и информацию о нем.**

**URL**: `/schedule/create`

**Method**: `POST`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Code**: `201 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода (вместо <integer> необходимо вписать нужные целочисленные значения, вместо <datetime> — дату и время, вместо <choice> — выбрать один из вариантов, предложенных в выпадающем списке):`

``` json
{
  "breedof_show": "<choice>",
  "timeof_show": "<datetime>",
  "numberof_ring": <integer>,
  "show_class": "<choice>",
  "show_schedule": <integer>
}
```
**End-point выводит список всех расписаний и информацию о них.**

**URL**: `/schedule/`

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
        "breedof_show": "Sobaka",
        "timeof_show": "2022-01-26T12:00:00Z",
        "numberof_ring": 1,
        "show_class": "Open",
        "show_schedule": 1
    },
    {
        "id": 2,
        "breedof_show": "Sobaka",
        "timeof_show": "2020-07-26T13:00:00Z",
        "numberof_ring": 2,
        "show_class": "Open",
        "show_schedule": 1
    }
]
```
**Таблица для хранения данных об оценках собак на выставке.**
 
`Таблица имеет следующие поля:`
  1.  "schedule" является внешним ключом к таблице ShowSchedule
  2.  "dog" является внешним ключом к таблице DogParticipation
  3.  "expert" является внешним ключом к таблице ExpertParticipation
  4.  "first" хранит оценку за упражнение №1
  5.  "second" хранит оценку за упражнение №2
  6.  "third" хранит оценку за упражнение №3
  7.  "sum" хранит информацию о сумме оценок за три упражнения

**End-point позволяет просмотреть подробную информацию об оценках, изменить её (одно поле или несколько) и удалить при необходимости.**

**URL**: `/grading/{id}/`

**Methods**: `GET, PUT, PATCH, DELETE`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Parameters**: `id` — ID оценивания

**Code GET**: `200 OK`

**Code PUT**: `200 OK`

**Code PATCH**: `200 OK`

**Code DELETE**: `204 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода для GET:`

``` json
{
    "id": 1,
    "first": 6,
    "second": 7,
    "third": 6,
    "sum": 19,
    "schedule": 1,
    "dog": 1,
    "expert": 67
}
```

`Ниже представлен пример вывода для PUT (вместо <integer> необходимо вписать нужные целочисленные значения):`

``` json
{
  "first": <integer>,
  "second": <integer>,
  "third": <integer>,
  "sum": <integer>,
  "schedule": <integer>,
  "dog": <integer>,
  "expert": <integer>
}
```

`Ниже представлен пример вывода для PATCH (вместо <integer> необходимо вписать нужные целочисленные значения):`

``` json
{
  "first": <integer>,
  "second": <integer>,
  "third": <integer>,
  "sum": <integer>,
  "schedule": <integer>,
  "dog": <integer>,
  "expert": <integer>
}
```
**End-point позволяет внести в систему новые оценки.**

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
  "first": <integer>,
  "second": <integer>,
  "third": <integer>,
  "sum": <integer>,
  "schedule": <integer>,
  "dog": <integer>,
  "expert": <integer>
}
```
**End-point выводит список всех оценок и информацию о них.**

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
        "first": 6,
        "second": 7,
        "third": 6,
        "sum": 19,
        "schedule": 1,
        "dog": 1,
        "expert": 67
    },
    {
        "id": 2,
        "grfirstade1": 8,
        "second": 8,
        "third": 6,
        "sum": 22,
        "schedule": 1,
        "dog": 3,
        "expert": 67
    }
]
```