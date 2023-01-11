# Изменить информацию о книге по ID

## Описание

```
url: /book/{id}/
method: PATCH
auth: Token, same Editor profile
```

## Пример запроса

```json
{
	"authors": [
		{
			"user": 12
		},
		{
			"user": 1
		}
	],
	"name": "My New Book"
}
```

## Успешный ответ
```
code: 200
```

```json
{
	"id": 1,
	"name": "My New Book",
	"authorships": [],
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