# Получить список всех менеджеров 

## Описание

```
url: /managers/
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
		"id": 4,
		"username": "user-3",
		"first_name": "Lesley",
		"last_name": "Sasser"
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
		"id": 10,
		"username": "user-9",
		"first_name": "Terra",
		"last_name": "Bullock"
	}
]
```