# Авторизовать пользователя

Авторизация пользователя

**URL** : `/auth/users/me/`

**Method** : `POST`

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
        "tel": "79129129121",
        "username": "first",
        "id": 3
    }
}
```