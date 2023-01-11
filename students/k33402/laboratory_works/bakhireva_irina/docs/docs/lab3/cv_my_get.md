# [ GET ] /cv/my/

## Информация

Получение резюме текущего пользователя

**Method**: `GET`  
**Authorization**: `Token`  
**Role**: `Applicant`

## Ответ

```json
{
	"user": {
		"id": 17,
		"first_name": "David",
		"last_name": "Norwood",
		"phone": "+7 123 456 7890",
		"email": "user@email.ru"
	},
	"work_history": [
		{
			"spec": null,
			"salary": 311000,
			"start_date": "2022-01-10T23:48:37.933059Z",
			"end_date": "2023-01-10T23:48:37.933059Z"
		},
		{
			"spec": {
				"id": 4,
				"name": "Программист Python",
				"level": 0,
				"level_name": "Junior"
			},
			"salary": 962000,
			"start_date": "2021-01-10T23:48:38.087694Z",
			"end_date": "2022-01-15T23:48:38.087694Z"
		},
		{
			"spec": {
				"id": 4,
				"name": "Программист Python",
				"level": 0,
				"level_name": "Junior"
			},
			"salary": 748000,
			"start_date": "2020-01-11T23:48:38.241337Z",
			"end_date": "2021-01-20T23:48:38.241337Z"
		},
		{
			"spec": {
				"id": 4,
				"name": "Программист Python",
				"level": 0,
				"level_name": "Junior"
			},
			"salary": 803000,
			"start_date": "2019-01-11T23:48:38.370269Z",
			"end_date": "2020-01-26T23:48:38.370269Z"
		},
		{
			"spec": {
				"id": 4,
				"name": "Программист Python",
				"level": 0,
				"level_name": "Junior"
			},
			"salary": 626000,
			"start_date": "2018-01-11T23:48:38.489129Z",
			"end_date": "2019-01-31T23:48:38.489129Z"
		},
		{
			"spec": null,
			"salary": 995000,
			"start_date": "2017-01-11T23:48:38.595088Z",
			"end_date": "2018-02-05T23:48:38.595088Z"
		},
		{
			"spec": null,
			"salary": 527000,
			"start_date": "2016-01-12T23:48:38.711093Z",
			"end_date": "2017-02-10T23:48:38.711093Z"
		},
		{
			"spec": {
				"id": 4,
				"name": "Программист Python",
				"level": 0,
				"level_name": "Junior"
			},
			"salary": 510000,
			"start_date": "2015-01-12T23:48:38.828290Z",
			"end_date": "2016-02-16T23:48:38.828290Z"
		},
		{
			"spec": {
				"id": 4,
				"name": "Программист Python",
				"level": 0,
				"level_name": "Junior"
			},
			"salary": 730000,
			"start_date": "2014-01-12T23:48:38.944088Z",
			"end_date": "2015-02-21T23:48:38.944088Z"
		},
		{
			"spec": {
				"id": 4,
				"name": "Программист Python",
				"level": 0,
				"level_name": "Junior"
			},
			"salary": 171000,
			"start_date": "2022-01-10T23:48:39.061182Z",
			"end_date": null
		}
	],
	"education": [
		{
			"education_level": "Middle",
			"description": "Прошел в ускоренном режиме",
			"start_date": "2014-01-12T23:48:37.778496Z",
			"end_date": "2015-01-12T23:48:37.778496Z"
		}
	],
	"courses": [
		{
			"course": {
				"id": 27,
				"name": "Получи профессию \"Программист JS( Senior )\"",
				"description": "Пройди этот курс и получи требуемую профессию за 2 дня!",
				"spec": {
					"id": 3,
					"name": "Программист JS(Senior)"
				},
				"required_spec": {
					"id": 2,
					"name": "Программист JS(Middle)"
				}
			},
			"start_date": "2017-10-10T23:48:39.187583Z",
			"end_date": "2017-10-14T23:48:39.187583Z"
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
			"start_date": "2012-11-10T23:48:39.327377Z",
			"end_date": "2012-11-14T23:48:39.327377Z"
		}
	],
	"id": 17
}
```