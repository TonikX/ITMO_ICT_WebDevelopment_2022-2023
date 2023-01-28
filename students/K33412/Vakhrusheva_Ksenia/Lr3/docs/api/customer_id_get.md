# Получить информацию о покупателе по ID пользователя

## Описание

```
url: /customer/{id}/
method: GET
auth: Token, Manager profile or same Customer profile
```

## Успешный ответ

```
code: 200
```

```json
{
	"user": {
		"id": 2,
		"username": "user-1",
		"first_name": "Earl",
		"last_name": "Rader"
	},
	"orders": [
		{
			"id": 4,
			"contracts": [
				{
					"id": 8,
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
						"id": 6,
						"username": "user-5",
						"first_name": "Marsha",
						"last_name": "Creed"
					},
					"creation_datetime": "2022-12-30T16:56:36.153958Z"
				},
				{
					"id": 9,
					"book": {
						"id": 13,
						"name": "Striped Greedy Turtle Of Temperance",
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
					"manager": {
						"id": 4,
						"username": "user-3",
						"first_name": "Lesley",
						"last_name": "Sasser"
					},
					"creation_datetime": "2022-12-30T16:56:36.259333Z"
				}
			]
		},
		{
			"id": 8,
			"contracts": [
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
					"manager": {
						"id": 5,
						"username": "user-4",
						"first_name": "Gwen",
						"last_name": "Zeigler"
					},
					"creation_datetime": "2022-12-30T16:56:38.060015Z"
				},
				{
					"id": 16,
					"book": {
						"id": 10,
						"name": "Meek Weasel Of Enjoyable Examination",
						"pages": 15,
						"illustrated": true,
						"authors": [
							{
								"user": 14,
								"pseudonym": "Willard Thrower"
							},
							{
								"user": 13,
								"pseudonym": "Mary Maloch"
							},
							{
								"user": 2,
								"pseudonym": "My Name Is John"
							}
						]
					},
					"manager": {
						"id": 2,
						"username": "user-1",
						"first_name": "Earl",
						"last_name": "Rader"
					},
					"creation_datetime": "2022-12-30T16:56:38.203348Z"
				},
				{
					"id": 17,
					"book": {
						"id": 1,
						"name": "My New Book",
						"pages": 15,
						"illustrated": true,
						"authors": []
					},
					"manager": {
						"id": 6,
						"username": "user-5",
						"first_name": "Marsha",
						"last_name": "Creed"
					},
					"creation_datetime": "2022-12-30T16:56:38.342066Z"
				}
			]
		},
		{
			"id": 10,
			"contracts": [
				{
					"id": 19,
					"book": {
						"id": 6,
						"name": "Sociable Invaluable Gibbon Of Gaiety",
						"pages": 15,
						"illustrated": true,
						"authors": [
							{
								"user": 14,
								"pseudonym": "Willard Thrower"
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
					"creation_datetime": "2022-12-30T16:56:38.586227Z"
				},
				{
					"id": 20,
					"book": {
						"id": 6,
						"name": "Sociable Invaluable Gibbon Of Gaiety",
						"pages": 15,
						"illustrated": true,
						"authors": [
							{
								"user": 14,
								"pseudonym": "Willard Thrower"
							},
							{
								"user": 10,
								"pseudonym": "Terra Bullock"
							}
						]
					},
					"manager": {
						"id": 6,
						"username": "user-5",
						"first_name": "Marsha",
						"last_name": "Creed"
					},
					"creation_datetime": "2022-12-30T16:56:38.713507Z"
				},
				{
					"id": 21,
					"book": {
						"id": 5,
						"name": "Quantum Overjoyed Pogona Of Strength",
						"pages": 15,
						"illustrated": true,
						"authors": [
							{
								"user": 14,
								"pseudonym": "Willard Thrower"
							},
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
					"manager": {
						"id": 2,
						"username": "user-1",
						"first_name": "Earl",
						"last_name": "Rader"
					},
					"creation_datetime": "2022-12-30T16:56:38.819273Z"
				}
			]
		},
		{
			"id": 11,
			"contracts": [
				{
					"id": 22,
					"book": {
						"id": 19,
						"name": "Premium Nano Scorpion Of Innovation",
						"pages": 15,
						"illustrated": true,
						"authors": [
							{
								"user": 13,
								"pseudonym": "Mary Maloch"
							}
						]
					},
					"manager": {
						"id": 10,
						"username": "user-9",
						"first_name": "Terra",
						"last_name": "Bullock"
					},
					"creation_datetime": "2022-12-30T16:56:38.935326Z"
				},
				{
					"id": 23,
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
					"manager": {
						"id": 6,
						"username": "user-5",
						"first_name": "Marsha",
						"last_name": "Creed"
					},
					"creation_datetime": "2022-12-30T16:56:39.095892Z"
				}
			]
		},
		{
			"id": 15,
			"contracts": [
				{
					"id": 30,
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
						"id": 2,
						"username": "user-1",
						"first_name": "Earl",
						"last_name": "Rader"
					},
					"creation_datetime": "2022-12-30T16:56:39.889264Z"
				}
			]
		},
		{
			"id": 19,
			"contracts": [
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
					"manager": {
						"id": 5,
						"username": "user-4",
						"first_name": "Gwen",
						"last_name": "Zeigler"
					},
					"creation_datetime": "2022-12-30T16:56:40.526344Z"
				}
			]
		}
	]
}
```