# Получить полную информацию об авторе по ID пользовователя

## Описание

```
url: /author/{id}/full/
method: GET
auth: Token, Manager profile or Editor profile or same Author profile
```

## Успешный ответ

```
code: 200
```

```json
{
	"user": 2,
	"pseudonym": "Earl Rader",
	"books": [
		{
			"id": 1,
			"name": "Whimsical Sweet Donkey Of Refinement",
			"contracts": 1
		},
		{
			"id": 2,
			"name": "Melodic Maroon Porpoise Of Wind",
			"contracts": 1
		},
		{
			"id": 3,
			"name": "Cautious Knowing Quoll Of Genius",
			"contracts": 2
		},
		{
			"id": 8,
			"name": "Wonderful Beryl Pelican Of Chemistry",
			"contracts": 1
		},
		{
			"id": 10,
			"name": "Meek Weasel Of Enjoyable Examination",
			"contracts": 1
		},
		{
			"id": 11,
			"name": "Crazy Silver Spoonbill Of Influence",
			"contracts": 2
		},
		{
			"id": 12,
			"name": "Armored Fair Cobra Of Fury",
			"contracts": 3
		},
		{
			"id": 14,
			"name": "Sassy Unselfish Unicorn Of Exercise",
			"contracts": 2
		}
	]
}
```