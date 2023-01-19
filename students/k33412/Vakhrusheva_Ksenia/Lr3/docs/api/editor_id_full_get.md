# Полуить полную информацию о редакторе по ID пользователя

## Описание

```
url: /editor/{id}/full/
method: GET
auth: Token, Manager profile or same Editor profile
```

## Успешный ответ

```
code: 200
```

```json
{
	"user": {
		"id": 6,
		"username": "user-5",
		"first_name": "Marsha",
		"last_name": "Creed"
	},
	"books": [
		{
			"id": 1,
			"name": "My New Book",
			"pages": 15,
			"illustrated": true,
			"authors": []
		},
		{
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
		{
			"id": 7,
			"name": "Unbiased Serious Squirrel Of Opposition",
			"pages": 15,
			"illustrated": true,
			"authors": [
				{
					"user": 5,
					"pseudonym": "Gwen Zeigler"
				},
				{
					"user": 14,
					"pseudonym": "Willard Thrower"
				},
				{
					"user": 13,
					"pseudonym": "Mary Maloch"
				}
			]
		},
		{
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
		{
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
		{
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
		{
			"id": 12,
			"name": "Armored Fair Cobra Of Fury",
			"pages": 15,
			"illustrated": true,
			"authors": [
				{
					"user": 2,
					"pseudonym": "My Name Is John"
				},
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
		{
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
		{
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
		{
			"id": 20,
			"name": "Colossal Bright Dingo Of Diversity",
			"pages": 15,
			"illustrated": true,
			"authors": [
				{
					"user": 10,
					"pseudonym": "Terra Bullock"
				},
				{
					"user": 14,
					"pseudonym": "Willard Thrower"
				}
			]
		}
	]
}
```