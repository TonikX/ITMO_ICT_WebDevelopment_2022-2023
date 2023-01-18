# Показать автора по ID пользователя
 
## Описание

```
url: /author/{id}
method: GET
auth: Token, Author profile
```

## Успешный ответ
```
code: 200
```

```json
[
	{
		"id": 1,
		"name": "My book",
		"pages": 15,
		"illustrated": true,
		"authors": [
			{
				"user": 8,
				"pseudonym": "My Name Is John"
			},
			{
				"user": 4,
				"pseudonym": "Sammie Williams"
			}
		]
	},
	{
		"id": 2,
		"name": "My New Book",
		"pages": 15,
		"illustrated": true,
		"authors": [
			{
				"user": 12,
				"pseudonym": "Carla Lancaster"
			}
		]
	}
]
```