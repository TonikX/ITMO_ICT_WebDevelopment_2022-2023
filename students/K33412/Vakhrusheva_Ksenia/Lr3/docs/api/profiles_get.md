# Получить все профили текущего пользователя

## Описание

```
url: /profiles/
method: GET
auth: Token
```

## Успешный ответ

```
code: 200
```

```json
{
	"author": null,
	"manager": {
		"id": 4,
		"username": "user-3",
		"first_name": "Lesley",
		"last_name": "Sasser"
	},
	"editor": null,
	"customer": null
}
```