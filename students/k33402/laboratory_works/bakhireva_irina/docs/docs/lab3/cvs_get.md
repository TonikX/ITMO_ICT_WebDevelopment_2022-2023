# [ GET ] /cvs/

## Информация

Получение списка всех резюме в системе

**Method**: `GET`  
**Authorization**: `Token`  
**Role**: `HR`

## Параметры

### В строке запроса

**specialization** - отображать только по конкретной специализации

## Ответ

```json
[
	{
		"user": {
			"id": 16,
			"first_name": "Dawn",
			"last_name": "Gardiner"
		},
		"specializations": [
			{
				"id": 2,
				"name": "Программист JS",
				"level": 1,
				"level_name": "Middle"
			},
			{
				"id": 4,
				"name": "Программист Python",
				"level": 0,
				"level_name": "Junior"
			},
			{
				"id": 6,
				"name": "Программист Python",
				"level": 2,
				"level_name": "Senior"
			}
		],
		"id": 16
	}
]
```