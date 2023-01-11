# [ GET ] /company/my/vacancys/

## Информация

Получение списка вакансий текущей компании HR агента

**Method**: `GET`  
**Authorization**: `Token`  
**Role**: `HR`

## Ответ

```json
[
	{
		"id": 6,
		"specs": [
			{
				"id": 4,
				"name": "Программист Python(Junior)"
			}
		],
		"salary": 843000,
		"created_date": "2023-01-10T20:48:05.297231Z",
		"closed_date": null
	},
	{
		"id": 7,
		"specs": [
			{
				"id": 1,
				"name": "Программист JS(Junior)"
			}
		],
		"salary": 811000,
		"created_date": "2023-01-10T20:48:05.558230Z",
		"closed_date": null
	},
	{
		"id": 8,
		"specs": [
			{
				"id": 7,
				"name": "Программист Unity(Junior)"
			}
		],
		"salary": 439000,
		"created_date": "2023-01-10T20:48:05.779734Z",
		"closed_date": null
	},
	{
		"id": 9,
		"specs": [
			{
				"id": 1,
				"name": "Программист JS(Junior)"
			}
		],
		"salary": 898000,
		"created_date": "2023-01-10T20:48:06.024732Z",
		"closed_date": null
	},
	{
		"id": 10,
		"specs": [
			{
				"id": 1,
				"name": "Программист JS(Junior)"
			}
		],
		"salary": 671000,
		"created_date": "2023-01-10T20:48:06.267403Z",
		"closed_date": null
	},
	{
		"id": 45,
		"specs": [
			{
				"id": 5,
				"name": "Программист Python(Middle)"
			},
			{
				"id": 6,
				"name": "Программист Python(Senior)"
			}
		],
		"salary": 1000,
		"created_date": "2023-01-10T21:51:39.854324Z",
		"closed_date": null
	},
	{
		"id": 46,
		"specs": [
			{
				"id": 5,
				"name": "Программист Python(Middle)"
			},
			{
				"id": 6,
				"name": "Программист Python(Senior)"
			}
		],
		"salary": 1000,
		"created_date": "2023-01-10T21:52:05.320251Z",
		"closed_date": null
	},
	{
		"id": 47,
		"specs": [
			{
				"id": 5,
				"name": "Программист Python(Middle)"
			},
			{
				"id": 6,
				"name": "Программист Python(Senior)"
			}
		],
		"salary": 1000000,
		"created_date": "2023-01-10T21:52:56.222411Z",
		"closed_date": null
	}
]
```