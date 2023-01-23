# Получить заказ по ID

## Описание

```
url: /order/{id}/
method: GET
auth: Token, Manager profile
```

## Успешный ответ

```
code: 200
```

```json
{
	"id": 1,
	"customer": {
		"id": 6,
		"username": "user-5",
		"first_name": "Marsha",
		"last_name": "Creed"
	},
	"contracts": [
		{
			"id": 1,
			"book": {
				"id": 15,
				"name": "Nice Astonishing Eel Of Science",
				"pages": 15,
				"illustrated": true,
				"authors": [
					{
						"user": 14,
						"pseudonym": "Willard Thrower"
					},
					{
						"user": 5,
						"pseudonym": "Gwen Zeigler"
					},
					{
						"user": 10,
						"pseudonym": "Terra Bullock"
					}
				]
			},
			"manager": {
				"id": 5,
				"username": "user-4",
				"first_name": "Gwen",
				"last_name": "Zeigler"
			},
			"creation_datetime": "2022-12-30T16:56:35.361301Z"
		},
		{
			"id": 2,
			"book": {
				"id": 14,
				"name": "Sassy Unselfish Unicorn Of Exercise",
				"pages": 15,
				"illustrated": true,
				"authors": [
					{
						"user": 2,
						"pseudonym": "My Name Is John"
					},
					{
						"user": 14,
						"pseudonym": "Willard Thrower"
					}
				]
			},
			"manager": {
				"id": 10,
				"username": "user-9",
				"first_name": "Terra",
				"last_name": "Bullock"
			},
			"creation_datetime": "2022-12-30T16:56:35.476985Z"
		},
		{
			"id": 3,
			"book": {
				"id": 15,
				"name": "Nice Astonishing Eel Of Science",
				"pages": 15,
				"illustrated": true,
				"authors": [
					{
						"user": 14,
						"pseudonym": "Willard Thrower"
					},
					{
						"user": 5,
						"pseudonym": "Gwen Zeigler"
					},
					{
						"user": 10,
						"pseudonym": "Terra Bullock"
					}
				]
			},
			"manager": {
				"id": 4,
				"username": "user-3",
				"first_name": "Lesley",
				"last_name": "Sasser"
			},
			"creation_datetime": "2022-12-30T16:56:35.593800Z"
		}
	]
}
```