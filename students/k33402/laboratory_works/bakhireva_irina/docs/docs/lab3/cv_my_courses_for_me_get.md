# [ GET ] /cv/my/courses_for_me/

## Информация

Получение списка доступных курсов для прохождения по текущему резюме соискателя

**Method**: `GET`  
**Authorization**: `Token`  
**Role**: `Applicant`

## Параметры

### В строке запроса

**specialization** - отображать только по конкретной специализации

## Ответ

```json
[
	{
		"id": 18,
		"name": "Получи профессию \"Программист JS( Middle )\"",
		"description": "Пройди этот курс и получи требуемую профессию за 2 дня!",
		"spec": {
			"id": 2,
			"name": "Программист JS(Middle)"
		},
		"required_spec": {
			"id": 1,
			"name": "Программист JS(Junior)"
		}
	},
	{
		"id": 20,
		"name": "Получи профессию \"Программист JS( Middle )\"",
		"description": "Пройди этот курс и получи требуемую профессию за 2 дня!",
		"spec": {
			"id": 2,
			"name": "Программист JS(Middle)"
		},
		"required_spec": {
			"id": 1,
			"name": "Программист JS(Junior)"
		}
	},
	{
		"id": 33,
		"name": "Получи профессию \"Программист JS( Middle )\"",
		"description": "Пройди этот курс и получи требуемую профессию за 2 дня!",
		"spec": {
			"id": 2,
			"name": "Программист JS(Middle)"
		},
		"required_spec": {
			"id": 1,
			"name": "Программист JS(Junior)"
		}
	},
	{
		"id": 41,
		"name": "Получи профессию \"Программист JS( Middle )\"",
		"description": "Пройди этот курс и получи требуемую профессию за 2 дня!",
		"spec": {
			"id": 2,
			"name": "Программист JS(Middle)"
		},
		"required_spec": {
			"id": 1,
			"name": "Программист JS(Junior)"
		}
	},
	{
		"id": 49,
		"name": "Получи профессию \"Программист JS( Middle )\"",
		"description": "Пройди этот курс и получи требуемую профессию за 2 дня!",
		"spec": {
			"id": 2,
			"name": "Программист JS(Middle)"
		},
		"required_spec": {
			"id": 1,
			"name": "Программист JS(Junior)"
		}
	},
	{
		"id": 50,
		"name": "Получи профессию \"Программист JS( Middle )\"",
		"description": "Пройди этот курс и получи требуемую профессию за 2 дня!",
		"spec": {
			"id": 2,
			"name": "Программист JS(Middle)"
		},
		"required_spec": {
			"id": 1,
			"name": "Программист JS(Junior)"
		}
	},
	{
		"id": 8,
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
	{
		"id": 17,
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
	{
		"id": 19,
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
	{
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
	{
		"id": 46,
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
	{
		"id": 23,
		"name": "Получи профессию \"Тестировщик\"",
		"description": "Пройди этот курс и получи требуемую профессию за 2 дня!",
		"spec": {
			"id": 10,
			"name": ""
		},
		"required_spec": {
			"id": 9,
			"name": "Программист Unity(Senior)"
		}
	}
]
```