# [ GET ] /company/{ID}

## Информация

Получение полной информации о компании по ее ID

**Method**: `GET`  
**Authorization**: `Token`  
**Role**: `-`

## Параметры

### В адресе

**ID** - идентификатор компании

## Ответ

```json
{
	"name": "Quirky Xanthic Mule Of Conversion",
	"address": "Москва, улица Пушкина",
	"hr": {
		"user": {
			"id": 1,
			"first_name": "Carol",
			"last_name": "Walsh",
			"phone": "+7 123 456 7890",
			"email": "user@email.ru"
		}
	},
	"vacancies": [
		{
			"id": 1,
			"specs": [
				{
					"id": 7,
					"name": "Программист Unity(Junior)"
				}
			],
			"salary": 967000,
			"created_date": "2023-01-10T20:48:03.209800Z",
			"closed_date": null
		},
		{
			"id": 2,
			"specs": [
				{
					"id": 9,
					"name": "Программист Unity(Senior)"
				}
			],
			"salary": 407000,
			"created_date": "2023-01-10T20:48:03.541335Z",
			"closed_date": null
		},
		{
			"id": 3,
			"specs": [
				{
					"id": 7,
					"name": "Программист Unity(Junior)"
				}
			],
			"salary": 462000,
			"created_date": "2023-01-10T20:48:03.795702Z",
			"closed_date": null
		},
		{
			"id": 4,
			"specs": [
				{
					"id": 2,
					"name": "Программист JS(Middle)"
				}
			],
			"salary": 293000,
			"created_date": "2023-01-10T20:48:04.040590Z",
			"closed_date": null
		},
		{
			"id": 5,
			"specs": [
				{
					"id": 1,
					"name": "Программист JS(Junior)"
				}
			],
			"salary": 505000,
			"created_date": "2023-01-10T20:48:04.315428Z",
			"closed_date": null
		}
	]
}
```