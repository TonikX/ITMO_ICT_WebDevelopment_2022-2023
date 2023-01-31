# [ POST ] /company/my/vacancys/

## Информация

Создание вакансии от лица компании

**Method**: `POST`  
**Authorization**: `Token`  
**Role**: `HR`

## Параметры

### В теле запроса

**educational_level** - уровень образования  
**seniority** - стаж  
**salary** - зарплата  
**description** - описание   
**specs** - специализации/профессии

## Запрос

```json
{
	"education_level": 2,
	"seniority": "Стаж 2 года",
	"salary": 1000000,
	"description": "Новая вакансия",
	"specs": [
		{
			"id": 5
		},
		{
			"id": 6
		}
	]
}
```

## Ответ

```json
{
	"company": {
		"id": 2,
		"name": "Psychedelic Beaver From Avalon"
	},
	"education_level": 2,
	"seniority": "Стаж 2 года",
	"salary": 1000000,
	"description": "Новая вакансия",
	"specs": [
		{
			"id": 5
		},
		{
			"id": 6
		}
	]
}
```