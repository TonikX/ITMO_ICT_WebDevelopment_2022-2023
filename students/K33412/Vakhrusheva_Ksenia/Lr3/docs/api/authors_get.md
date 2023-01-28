# Получить список всех авторов и их книг

## Описание

```
url: /authors/
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
		"user": 2,
		"pseudonym": "My Name Is John",
		"books": [
			{
				"id": 1,
				"name": "Whimsical Sweet Donkey Of Refinement"
			},
			{
				"id": 2,
				"name": "Melodic Maroon Porpoise Of Wind"
			},
			{
				"id": 3,
				"name": "Cautious Knowing Quoll Of Genius"
			},
			{
				"id": 8,
				"name": "Wonderful Beryl Pelican Of Chemistry"
			},
			{
				"id": 10,
				"name": "Meek Weasel Of Enjoyable Examination"
			},
			{
				"id": 11,
				"name": "Crazy Silver Spoonbill Of Influence"
			},
			{
				"id": 12,
				"name": "Armored Fair Cobra Of Fury"
			},
			{
				"id": 14,
				"name": "Sassy Unselfish Unicorn Of Exercise"
			}
		]
	}
]
```