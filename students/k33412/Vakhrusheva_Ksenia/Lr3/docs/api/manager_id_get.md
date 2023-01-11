# Получить информацию о менеджере по ID пользователя

## Описание

```
url: /manager/{id}/
method: GET
auth: Token, Manager profile
```

## Успешный ответ

```
code: 200
```

```json
{
	"user": {
		"id": 5,
		"username": "user-4",
		"first_name": "Gwen",
		"last_name": "Zeigler"
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
			"creation_datetime": "2022-12-30T16:56:35.361301Z"
		},
		{
			"id": 12,
			"book": {
				"id": 18,
				"name": "Illustrious Boa Of Imaginary Calibration",
				"pages": 15,
				"illustrated": true,
				"authors": [
					{
						"user": 10,
						"pseudonym": "Terra Bullock"
					},
					{
						"user": 13,
						"pseudonym": "Mary Maloch"
					}
				]
			},
			"creation_datetime": "2022-12-30T16:56:36.622536Z"
		},
		{
			"id": 15,
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
			"creation_datetime": "2022-12-30T16:56:38.060015Z"
		},
		{
			"id": 34,
			"book": {
				"id": 11,
				"name": "Crazy Silver Spoonbill Of Influence",
				"pages": 15,
				"illustrated": true,
				"authors": [
					{
						"user": 10,
						"pseudonym": "Terra Bullock"
					},
					{
						"user": 5,
						"pseudonym": "Gwen Zeigler"
					},
					{
						"user": 2,
						"pseudonym": "My Name Is John"
					}
				]
			},
			"creation_datetime": "2022-12-30T16:56:40.366153Z"
		},
		{
			"id": 35,
			"book": {
				"id": 9,
				"name": "Light Grinning Alpaca Of Karma",
				"pages": 15,
				"illustrated": true,
				"authors": [
					{
						"user": 13,
						"pseudonym": "Mary Maloch"
					},
					{
						"user": 5,
						"pseudonym": "Gwen Zeigler"
					}
				]
			},
			"creation_datetime": "2022-12-30T16:56:40.526344Z"
		},
		{
			"id": 36,
			"book": {
				"id": 8,
				"name": "Wonderful Beryl Pelican Of Chemistry",
				"pages": 15,
				"illustrated": true,
				"authors": [
					{
						"user": 5,
						"pseudonym": "Gwen Zeigler"
					},
					{
						"user": 2,
						"pseudonym": "My Name Is John"
					}
				]
			},
			"creation_datetime": "2022-12-30T16:56:40.632322Z"
		}
	]
}
```