**Данная конечная точка выводит отчёт по конкретной выставке.**

`Данная конечная точка выводит:`
:

  1. Название выставки и год её проведения

  2. Общее количество участников 

  3. Количество участников по каждой породе

  4. Оценки всех участников

  5. Медали, завоеванные участниками

**URL**: `/report/{id}`

**Method**: `GET`

**Auth required**: `No`

**Permissions required**: `No`

**Data constraints**: `{}`

**Parameters**: `id` — идентификатор нужной выставки

**Code**: `200 OK`

**Content**: `{[]}`

`Ниже представлен пример вывода:`

``` json
{
    "show_title": "Doggy Show",
    "year": 2020,
    "participants_number": 10,
    "breeds": [
        {
            "participant_dog__breed": "Корги/Corgi",
            "count": 3
        },
        {
            "participant_dog__breed": "Пудель/Poodle",
            "count": 1
        },
        {
            "participant_dog__breed": "Ретривер/Retriever",
            "count": 3
        },
        {
            "participant_dog__breed": "Самоед/Samoyed",
            "count": 3
        }
    ],
    "best_grades": [
        {
            "dog_grade__participant_dog__dog_name": "Fluffy",
            "dog_grade__participant_dog__breed": "Корги/Corgi",
            "dog_grade__id": 1,
            "grade1": 6,
            "grade2": 7,
            "grade3": 6,
            "sum": 19
        },
        {
            "dog_grade__participant_dog__dog_name": "Coffee",
            "dog_grade__participant_dog__breed": "Корги/Corgi",
            "dog_grade__id": 3,
            "grade1": 8,
            "grade2": 8,
            "grade3": 6,
            "sum": 22
        },
        {
            "dog_grade__participant_dog__dog_name": "Leo",
            "dog_grade__participant_dog__breed": "Корги/Corgi",
            "dog_grade__id": 2,
            "grade1": 9,
            "grade2": 9,
            "grade3": 5,
            "sum": 23
        },
        {
            "dog_grade__participant_dog__dog_name": "Finn",
            "dog_grade__participant_dog__breed": "Ретривер/Retriever",
            "dog_grade__id": 9,
            "grade1": 8,
            "grade2": 7,
            "grade3": 6,
            "sum": 21
        },
        {
            "dog_grade__participant_dog__dog_name": "Teddy",
            "dog_grade__participant_dog__breed": "Ретривер/Retriever",
            "dog_grade__id": 7,
            "grade1": 8,
            "grade2": 8,
            "grade3": 8,
            "sum": 24
        },
        {
            "dog_grade__participant_dog__dog_name": "Zeus",
            "dog_grade__participant_dog__breed": "Ретривер/Retriever",
            "dog_grade__id": 8,
            "grade1": 9,
            "grade2": 9,
            "grade3": 9,
            "sum": 27
        },
        {
            "dog_grade__participant_dog__dog_name": "Cookie",
            "dog_grade__participant_dog__breed": "Самоед/Samoyed",
            "dog_grade__id": 5,
            "grade1": 9,
            "grade2": 7,
            "grade3": 6,
            "sum": 22
        },
        {
            "dog_grade__participant_dog__dog_name": "Cloudy",
            "dog_grade__participant_dog__breed": "Самоед/Samoyed",
            "dog_grade__id": 4,
            "grade1": 8,
            "grade2": 8,
            "grade3": 8,
            "sum": 24
        },
        {
            "dog_grade__participant_dog__dog_name": "Snow",
            "dog_grade__participant_dog__breed": "Самоед/Samoyed",
            "dog_grade__id": 6,
            "grade1": 10,
            "grade2": 10,
            "grade3": 9,
            "sum": 29
        }
    ],
    "medals": [
        {
            "participant_dog__dog_name": "Fluffy",
            "participant_dog__breed": "Корги/Corgi",
            "show_medal": "Бронза/Bronze",
            "medals_count": 1
        },
        {
            "participant_dog__dog_name": "Coffee",
            "participant_dog__breed": "Корги/Corgi",
            "show_medal": "Серебро/Silver",
            "medals_count": 1
        },
        {
            "participant_dog__dog_name": "Leo",
            "participant_dog__breed": "Корги/Corgi",
            "show_medal": "Золото/Gold",
            "medals_count": 1
        },
        {
            "participant_dog__dog_name": "Storm",
            "participant_dog__breed": "Пудель/Poodle",
            "show_medal": null,
            "medals_count": 0
        },
        {
            "participant_dog__dog_name": "Finn",
            "participant_dog__breed": "Ретривер/Retriever",
            "show_medal": "Бронза/Bronze",
            "medals_count": 1
        },
        {
            "participant_dog__dog_name": "Teddy",
            "participant_dog__breed": "Ретривер/Retriever",
            "show_medal": "Серебро/Silver",
            "medals_count": 1
        },
        {
            "participant_dog__dog_name": "Zeus",
            "participant_dog__breed": "Ретривер/Retriever",
            "show_medal": "Золото/Gold",
            "medals_count": 1
        },
        {
            "participant_dog__dog_name": "Cookie",
            "participant_dog__breed": "Самоед/Samoyed",
            "show_medal": "Бронза/Bronze",
            "medals_count": 1
        },
        {
            "participant_dog__dog_name": "Cloudy",
            "participant_dog__breed": "Самоед/Samoyed",
            "show_medal": "Серебро/Silver",
            "medals_count": 1
        },
        {
            "participant_dog__dog_name": "Snow",
            "participant_dog__breed": "Самоед/Samoyed",
            "show_medal": "Золото/Gold",
            "medals_count": 1
        }
    ]
}
```