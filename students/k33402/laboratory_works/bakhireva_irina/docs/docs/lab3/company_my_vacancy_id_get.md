# [ GET ] /company/my/vacancy/{ID}/

## Информация

Получение информации о вакансии, которая принадлежит текущей компании HR агента

**Method**: `GET`  
**Authorization**: `Token`  
**Role**: `HR`

## Параметры

### В адресе

**ID** - идентификатор вакансии

## Ответ

```json
{
	"id": 47,
	"company": {
		"id": 2,
		"hr": {
			"user": {
				"id": 2,
				"first_name": "Thomas",
				"last_name": "Clifton",
				"phone": "+7 123 456 7890",
				"email": "user@email.ru"
			}
		},
		"name": "Psychedelic Beaver From Avalon",
		"address": "Москва, улица Пушкина"
	},
	"education_level": "Master",
	"specs": [
		{
			"id": 3,
			"name": "Программист JS",
			"level": 2,
			"level_name": "Senior"
		}
	],
	"seniority": "Стаж 2 года",
	"salary": 2000000,
	"description": "Новое описание",
	"created_date": "2023-01-10T21:52:56.222411Z",
	"closed_date": null
}
```