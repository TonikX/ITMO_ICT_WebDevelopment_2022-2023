# Получить информацию о книге по ID

## Описание

```
url: /book/{id}/
method: GET
auth: no
```

## Успешный ответ

```
code: 200
```

```json
{
	"id": 1,
	"name": "Whimsical Sweet Donkey Of Refinement",
	"pages": 15,
	"illustrated": true,
	"authors": [
		{
			"user": 10,
			"pseudonym": "Terra Bullock"
		},
		{
			"user": 2,
			"pseudonym": "My Name Is John"
		}
	]
}
```