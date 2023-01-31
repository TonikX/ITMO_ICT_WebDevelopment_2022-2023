# [ GET ] /courses/

## Информация

Получение списка курсов в системе

**Method**: `GET`  
**Authorization**: `Token`  
**Role**: `-`

## Параметры

### В строке запроса

**specialization** - отображать только по конкретной специализации

## Ответ

```json
[
	{
		"id": 1,
		"name": "Получи профессию \"Программист Python( Senior )\"",
		"description": "Пройди этот курс и получи требуемую профессию за 2 дня!",
		"spec": {
			"id": 6,
			"name": "Программист Python(Senior)"
		},
		"required_spec": {
			"id": 6,
			"name": "Программист Python(Senior)"
		}
	},
	{
		"id": 2,
		"name": "Получи профессию \"Программист Python( Senior )\"",
		"description": "Пройди этот курс и получи требуемую профессию за 2 дня!",
		"spec": {
			"id": 6,
			"name": "Программист Python(Senior)"
		},
		"required_spec": {
			"id": 6,
			"name": "Программист Python(Senior)"
		}
	},
	{
		"id": 21,
		"name": "Получи профессию \"Программист Python( Senior )\"",
		"description": "Пройди этот курс и получи требуемую профессию за 2 дня!",
		"spec": {
			"id": 6,
			"name": "Программист Python(Senior)"
		},
		"required_spec": {
			"id": 6,
			"name": "Программист Python(Senior)"
		}
	},
	{
		"id": 28,
		"name": "Получи профессию \"Программист Python( Senior )\"",
		"description": "Пройди этот курс и получи требуемую профессию за 2 дня!",
		"spec": {
			"id": 6,
			"name": "Программист Python(Senior)"
		},
		"required_spec": {
			"id": 6,
			"name": "Программист Python(Senior)"
		}
	},
	{
		"id": 41,
		"name": "Получи профессию \"Программист Python( Senior )\"",
		"description": "Пройди этот курс и получи требуемую профессию за 2 дня!",
		"spec": {
			"id": 6,
			"name": "Программист Python(Senior)"
		},
		"required_spec": {
			"id": 6,
			"name": "Программист Python(Senior)"
		}
	}
]
```