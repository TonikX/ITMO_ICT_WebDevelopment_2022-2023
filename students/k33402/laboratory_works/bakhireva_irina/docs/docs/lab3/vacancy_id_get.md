# [ GET ] /vacancy/{ID}/

## Информация

Получение информации о вакансии по ID

**Method**: `GET`  
**Authorization**: `Token`  
**Role**: `-`

## Ответ

```json
{
	"id": 2,
	"company": {
		"id": 1,
		"hr": {
			"user": {
				"first_name": "Efrain",
				"last_name": "Brown",
				"phone": "+7 123 456 7890",
				"email": "user@email.ru"
			}
		},
		"name": "Polite Pygmy Lori Of Engineering",
		"address": "Москва, улица Пушкина"
	},
	"education_level": "Master",
	"specs": [
		{
			"id": 8,
			"name": "Программист Unity",
			"level": 1,
			"level_name": "Middle"
		}
	],
	"seniority": "Требуемый стаж 6 лет",
	"salary": 547000,
	"description": "Требуется сотрудник на полную занятость",
	"created_date": "2023-01-10T18:16:24.284857Z",
	"closed_date": null
}
```