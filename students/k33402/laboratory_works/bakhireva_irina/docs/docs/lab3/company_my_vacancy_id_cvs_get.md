# [ GET ] /company/my/vacancy/{ID}/cvs/

## Информация

Получение списка резюме, подходящих под вакансию

**Method**: `GET`  
**Authorization**: `Token`  
**Role**: `HR`

## Параметры

### В адресе

**ID** - идентификатор вакансии

## Ответ

```json
[
	{
		"user": {
			"id": 32,
			"first_name": "Mary",
			"last_name": "Nettles",
			"phone": "+7 123 456 7890",
			"email": "user@email.ru"
		},
		"work_history": [
			{
				"spec": {
					"id": 3,
					"name": "Программист JS",
					"level": 2,
					"level_name": "Senior"
				},
				"salary": 554000,
				"start_date": "2022-01-10T23:49:09.804439Z",
				"end_date": "2023-01-10T23:49:09.804439Z"
			},
			{
				"spec": {
					"id": 3,
					"name": "Программист JS",
					"level": 2,
					"level_name": "Senior"
				},
				"salary": 380000,
				"start_date": "2021-01-10T23:49:09.932222Z",
				"end_date": "2022-01-15T23:49:09.932222Z"
			},
			{
				"spec": {
					"id": 3,
					"name": "Программист JS",
					"level": 2,
					"level_name": "Senior"
				},
				"salary": 797000,
				"start_date": "2020-01-11T23:49:10.040101Z",
				"end_date": "2021-01-20T23:49:10.040101Z"
			},
			{
				"spec": null,
				"salary": 405000,
				"start_date": "2019-01-11T23:49:10.178340Z",
				"end_date": "2020-01-26T23:49:10.178620Z"
			},
			{
				"spec": {
					"id": 3,
					"name": "Программист JS",
					"level": 2,
					"level_name": "Senior"
				},
				"salary": 447000,
				"start_date": "2018-01-11T23:49:10.328247Z",
				"end_date": "2019-01-31T23:49:10.328247Z"
			},
			{
				"spec": {
					"id": 3,
					"name": "Программист JS",
					"level": 2,
					"level_name": "Senior"
				},
				"salary": 49000,
				"start_date": "2017-01-11T23:49:10.456108Z",
				"end_date": "2018-02-05T23:49:10.456108Z"
			},
			{
				"spec": {
					"id": 3,
					"name": "Программист JS",
					"level": 2,
					"level_name": "Senior"
				},
				"salary": 289000,
				"start_date": "2016-01-12T23:49:10.561102Z",
				"end_date": "2017-02-10T23:49:10.561102Z"
			},
			{
				"spec": null,
				"salary": 557000,
				"start_date": "2015-01-12T23:49:10.666101Z",
				"end_date": "2016-02-16T23:49:10.666101Z"
			},
			{
				"spec": {
					"id": 3,
					"name": "Программист JS",
					"level": 2,
					"level_name": "Senior"
				},
				"salary": 728000,
				"start_date": "2014-01-12T23:49:10.794143Z",
				"end_date": "2015-02-21T23:49:10.794143Z"
			},
			{
				"spec": null,
				"salary": 163000,
				"start_date": "2022-01-10T23:49:10.982661Z",
				"end_date": null
			}
		],
		"education": [
			{
				"education_level": "Master",
				"description": "Прошел в ускоренном режиме",
				"start_date": "2021-01-10T23:49:09.675966Z",
				"end_date": "2022-01-10T23:49:09.675966Z"
			}
		],
		"courses": [
			{
				"course": {
					"id": 42,
					"name": "Получи профессию \"Программист Python( Middle )\"",
					"description": "Пройди этот курс и получи требуемую профессию за 2 дня!",
					"spec": {
						"id": 5,
						"name": "Программист Python(Middle)"
					},
					"required_spec": {
						"id": 4,
						"name": "Программист Python(Junior)"
					}
				},
				"start_date": "2011-11-21T23:49:11.369144Z",
				"end_date": "2011-11-25T23:49:11.369144Z"
			},
			{
				"course": {
					"id": 29,
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
				"start_date": "2012-06-04T23:49:11.544550Z",
				"end_date": "2012-06-08T23:49:11.544550Z"
			},
			{
				"course": {
					"id": 37,
					"name": "Получи профессию \"Программист Unity( Senior )\"",
					"description": "Пройди этот курс и получи требуемую профессию за 2 дня!",
					"spec": {
						"id": 9,
						"name": "Программист Unity(Senior)"
					},
					"required_spec": {
						"id": 8,
						"name": "Программист Unity(Middle)"
					}
				},
				"start_date": "2014-12-29T23:49:11.677233Z",
				"end_date": "2015-01-02T23:49:11.677233Z"
			}
		],
		"id": 32
	}
]
```