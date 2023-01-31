# [ GET ] /cv/my/specializations/

## Информация

Получение списка профессий, доступных для трудоустройства по текущему резюме соискателя

**Method**: `GET`  
**Authorization**: `Token`  
**Role**: `Applicant`

## Ответ

```json
[
	{
		"id": 3,
		"name": "Программист JS",
		"level": 2,
		"level_name": "Senior"
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
]
```