# Получить полную информацию о книге по ID

## Описание

```
url: /book/{id}/full/
method: GET
auth: Token, Manager profile or Editor profile or same Author profile
```

## Успешный ответ

```
code: 200
```

```json
{
	"id": 1,
	"name": "Whimsical Sweet Donkey Of Refinement",
	"authorships": [
		{
			"user": 10,
			"pseudonym": "Terra Bullock",
			"priority": 0
		},
		{
			"user": 2,
			"pseudonym": "My Name Is John",
			"priority": 1
		}
	],
	"main_editor": {
		"id": 12,
		"username": "user-11",
		"first_name": "Albert",
		"last_name": "Darnell"
	},
	"editors": [
		{
			"id": 12,
			"username": "user-11",
			"first_name": "Albert",
			"last_name": "Darnell"
		},
		{
			"id": 6,
			"username": "user-5",
			"first_name": "Marsha",
			"last_name": "Creed"
		},
		{
			"id": 11,
			"username": "user-10",
			"first_name": "Jack",
			"last_name": "Lehman"
		}
	],
	"pages": 15,
	"illustrated": true
}
```