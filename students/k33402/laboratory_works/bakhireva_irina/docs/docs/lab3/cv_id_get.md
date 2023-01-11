# [ GET ] /cv/{ID}/

## Информация

Получение информации о резюме по его ID

**Method**: `GET`  
**Authorization**: `Token`  
**Role**: `HR`

## Параметры

### В адресе

**ID** - идентификатор резюме

## Ответ

```json
{
	"user": {
		"id": 16,
		"first_name": "Dawn",
		"last_name": "Gardiner",
		"phone": "+7 123 456 7890",
		"email": "user@email.ru"
	},
	"work_history": [
		{
			"spec": {
				"id": 2,
				"name": "Программист JS",
				"level": 1,
				"level_name": "Middle"
			},
			"salary": 619000,
			"start_date": "2022-01-10T23:48:35.218802Z",
			"end_date": "2023-01-10T23:48:35.218802Z"
		},
		{
			"spec": null,
			"salary": 461000,
			"start_date": "2021-01-10T23:48:35.351402Z",
			"end_date": "2022-01-15T23:48:35.351402Z"
		},
		{
			"spec": null,
			"salary": 894000,
			"start_date": "2020-01-11T23:48:35.501298Z",
			"end_date": "2021-01-20T23:48:35.501298Z"
		},
		{
			"spec": null,
			"salary": 1000000,
			"start_date": "2022-01-10T23:48:35.616796Z",
			"end_date": null
		}
	],
	"education": [
		{
			"education_level": "Master",
			"description": "Прошел в ускоренном режиме",
			"start_date": "2013-01-12T23:48:35.085870Z",
			"end_date": "2014-01-12T23:48:35.085870Z"
		}
	],
	"courses": [
		{
			"course": {
				"id": 10,
				"name": "Получи профессию \"Программист Python( Junior )\"",
				"description": "Пройди этот курс и получи требуемую профессию за 2 дня!",
				"spec": {
					"id": 4,
					"name": "Программист Python(Junior)"
				},
				"required_spec": {
					"id": 3,
					"name": "Программист JS(Senior)"
				}
			},
			"start_date": "2013-03-18T23:48:35.760299Z",
			"end_date": "2013-03-22T23:48:35.760299Z"
		},
		{
			"course": {
				"id": 48,
				"name": "Получи профессию \"Программист Python( Senior )\"",
				"description": "Пройди этот курс и получи требуемую профессию за 2 дня!",
				"spec": {
					"id": 6,
					"name": "Программист Python(Senior)"
				},
				"required_spec": {
					"id": 5,
					"name": "Программист Python(Middle)"
				}
			},
			"start_date": "2013-04-04T23:48:35.892550Z",
			"end_date": "2013-04-08T23:48:35.892550Z"
		}
	],
	"id": 16
}
```