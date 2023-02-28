# Получить список всех покупателей

## Описание

```
url: /customers/
method: GET
auth: Token, Manager profile
```

## Успешный ответ

```
code: 200
```

```json
[
	{
		"id": 5,
		"username": "user-4",
		"first_name": "Gwen",
		"last_name": "Zeigler"
	},
	{
		"id": 2,
		"username": "user-1",
		"first_name": "Earl",
		"last_name": "Rader"
	},
	{
		"id": 6,
		"username": "user-5",
		"first_name": "Marsha",
		"last_name": "Creed"
	},
	{
		"id": 8,
		"username": "user-7",
		"first_name": "Kathryn",
		"last_name": "Rickey"
	},
	{
		"id": 13,
		"username": "user-12",
		"first_name": "Mary",
		"last_name": "Maloch"
	}
]
```