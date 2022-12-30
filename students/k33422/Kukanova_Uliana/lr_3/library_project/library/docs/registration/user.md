# Создать пользователя

Регистрирует пользователя

**URL** : `/auth/users/`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `201 Created`

**Content** : `{}`

```json
{
   "User":
    {
        "first_name": "Ivan",
        "last_name": "Ivanov",
        "tel": "79129129121",
        "username": "first",
        "id": 3
    }
}
```