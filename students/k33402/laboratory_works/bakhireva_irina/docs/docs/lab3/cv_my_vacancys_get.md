# [ GET ] /cv/my/vacancys/

## Информация

Получение списка доступных вакансий по текущему резюме соискателя

**Method**: `GET`  
**Authorization**: `Token`  
**Role**: `Applicant`

## Ответ

```json
[
	{
		"id": 17,
		"company": {
			"id": 6,
			"hr": {
				"user": {
					"id": 6,
					"first_name": "Tammy",
					"last_name": "Mantini",
					"phone": "+7 123 456 7890",
					"email": "user@email.ru"
				}
			},
			"name": "Frisky Locust Of Imminent Control",
			"address": "Москва, улица Пушкина"
		},
		"education_level": "Middle",
		"specs": [
			{
				"id": 3,
				"name": "Программист JS",
				"level": 2,
				"level_name": "Senior"
			}
		],
		"seniority": "Требуемый стаж 6 лет",
		"salary": 459000,
		"description": "Требуется сотрудник на полную занятость",
		"created_date": "2023-01-10T20:48:12.185396Z",
		"closed_date": null
	},
	{
		"id": 30,
		"company": {
			"id": 10,
			"hr": {
				"user": {
					"id": 10,
					"first_name": "Janet",
					"last_name": "Mazon",
					"phone": "+7 123 456 7890",
					"email": "user@email.ru"
				}
			},
			"name": "Clever Wildcat Of Perpetual Serenity",
			"address": "Москва, улица Пушкина"
		},
		"education_level": "Middle",
		"specs": [
			{
				"id": 3,
				"name": "Программист JS",
				"level": 2,
				"level_name": "Senior"
			}
		],
		"seniority": "Требуемый стаж 6 лет",
		"salary": 737000,
		"description": "Требуется сотрудник на полную занятость",
		"created_date": "2023-01-10T20:48:19.537805Z",
		"closed_date": null
	},
	{
		"id": 6,
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
		"education_level": "Middle",
		"specs": [
			{
				"id": 4,
				"name": "Программист Python",
				"level": 0,
				"level_name": "Junior"
			}
		],
		"seniority": "Требуемый стаж 6 лет",
		"salary": 843000,
		"description": "Требуется сотрудник на полную занятость",
		"created_date": "2023-01-10T20:48:05.297231Z",
		"closed_date": null
	},
	{
		"id": 15,
		"company": {
			"id": 5,
			"hr": {
				"user": {
					"id": 5,
					"first_name": "Irma",
					"last_name": "Marshall",
					"phone": "+7 123 456 7890",
					"email": "user@email.ru"
				}
			},
			"name": "Military Valiant Slug Of Gallantry",
			"address": "Москва, улица Пушкина"
		},
		"education_level": "Middle",
		"specs": [
			{
				"id": 4,
				"name": "Программист Python",
				"level": 0,
				"level_name": "Junior"
			}
		],
		"seniority": "Требуемый стаж 6 лет",
		"salary": 933000,
		"description": "Требуется сотрудник на полную занятость",
		"created_date": "2023-01-10T20:48:10.867326Z",
		"closed_date": null
	},
	{
		"id": 39,
		"company": {
			"id": 13,
			"hr": {
				"user": {
					"id": 13,
					"first_name": "Mildred",
					"last_name": "Sprenger",
					"phone": "+7 123 456 7890",
					"email": "user@email.ru"
				}
			},
			"name": "Enlightened Romantic Iguana From Tartarus",
			"address": "Москва, улица Пушкина"
		},
		"education_level": "Middle",
		"specs": [
			{
				"id": 4,
				"name": "Программист Python",
				"level": 0,
				"level_name": "Junior"
			}
		],
		"seniority": "Требуемый стаж 6 лет",
		"salary": 959000,
		"description": "Требуется сотрудник на полную занятость",
		"created_date": "2023-01-10T20:48:23.798402Z",
		"closed_date": null
	}
]
```