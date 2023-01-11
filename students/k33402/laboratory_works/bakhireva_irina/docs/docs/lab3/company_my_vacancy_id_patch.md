# [ PATCH ] /company/my/vacancy/{ID}/

## Информация

Редактирование информации о вакансии от текущей компании HR агента

**Method**: `Patch`  
**Authorization**: `Token`  
**Role**: `HR`

## Параметры

### В адресе

**ID** - идентификатор вакансии

### В теле запроса

**educational_level** - уровень образования  
**seniority** - стаж  
**salary** - зарплата  
**description** - описание   
**specs** - специализации/профессии

## Запрос

```json
{
	"specs": [
		{
			"id": 3
		}
	],
	"salary": 2000000,
	"description": "Новое описание",
	"education_level": 4
}
```

## Ответ

```json
{
	"message": "ok"
}
```