# Получить список всех книг и их авторов

## Описание

```
url: /books/
method: GET
auth: no
```

## Успешный ответ

```
code: 200
```

```json
[
	{
		"id": 1,
		"name": "My New Book",
		"pages": 15,
		"illustrated": true,
		"authors": []
	},
	{
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
	}
]
```