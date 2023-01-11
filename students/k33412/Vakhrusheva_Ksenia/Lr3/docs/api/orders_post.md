# Создать заказ

## Описание

```
url: /orders/
method: POST
auth: Token, Customer profile
```

## Пример запроса

```json
{
	"contracts": [
		{
			"book": 1
		},
		{
			"book": 2
		}
	]
}
```

## Успешный ответ

```
code: 201
```

```json
{
	"id": 21,
	"contracts": [
		{
			"id": 37,
			"book": {
				"id": 1,
				"name": "My New Book",
				"pages": 15,
				"illustrated": true,
				"authors": []
			},
			"manager": {
				"id": 4,
				"username": "user-3",
				"first_name": "Lesley",
				"last_name": "Sasser"
			},
			"creation_datetime": "2022-12-30T18:01:54.234480Z"
		},
		{
			"id": 38,
			"book": {
				"id": 2,
				"name": "Melodic Maroon Porpoise Of Wind",
				"pages": 15,
				"illustrated": true,
				"authors": [
					{
						"user": 14,
						"pseudonym": "Willard Thrower"
					},
					{
						"user": 2,
						"pseudonym": "My Name Is John"
					},
					{
						"user": 5,
						"pseudonym": "Gwen Zeigler"
					}
				]
			},
			"manager": {
				"id": 4,
				"username": "user-3",
				"first_name": "Lesley",
				"last_name": "Sasser"
			},
			"creation_datetime": "2022-12-30T18:01:54.388596Z"
		}
	]
}
```