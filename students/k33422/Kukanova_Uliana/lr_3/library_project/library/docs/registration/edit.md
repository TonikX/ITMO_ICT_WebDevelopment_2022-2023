# Изменить учетные данные пользователя

Изменяются учетные данные пользователя

**URL** : `/auth/users/me/`

**Method** : `PATCH`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{}`

```json
{
   "User":
    {
        "first_name": "Ivan",
        "last_name": "Ivanov",
        "tel": "+79219219212",
        "id": 3,
        "username": "first"
    }
}
```