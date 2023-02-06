from drf_yasg import openapi

user_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['username', 'password'],
    properties={
        "id": openapi.Schema(type=openapi.TYPE_NUMBER),
        "username": openapi.Schema(type=openapi.TYPE_STRING),
        "password": openapi.Schema(type=openapi.TYPE_STRING),
        "email": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_EMAIL),

        "last_name": openapi.Schema(type=openapi.TYPE_STRING),
        "first_name": openapi.Schema(type=openapi.TYPE_STRING),
        "middle_name": openapi.Schema(type=openapi.TYPE_STRING),

        "serial_number": openapi.Schema(type=openapi.TYPE_STRING),
        "passport": openapi.Schema(type=openapi.TYPE_STRING),
        "address": openapi.Schema(type=openapi.TYPE_STRING),
        "education_level": openapi.Schema(type=openapi.TYPE_STRING),
        "phone_number": openapi.Schema(type=openapi.TYPE_STRING),
        "academic_degree": openapi.Schema(type=openapi.TYPE_STRING),
        "date_of_birth": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE),
        "library": openapi.Schema(type=openapi.TYPE_NUMBER),
        "reading_room": openapi.Schema(type=openapi.TYPE_NUMBER),

        "readingroombookuser_set": openapi.Schema(type=openapi.TYPE_STRING),
    },
)

USERS_RESPONSES_GET = {
    "200": openapi.Response(
        description="custom 200 description",
        examples={
            "application/json": {
                "User": [
                    {
                        "id": 3,
                        "username": "test",
                        "email": "",
                        "last_name": "",
                        "first_name": "",
                        "middle_name": "",
                        "serial_number": "0000",
                        "passport": "",
                        "address": "",
                        "education_level": "",
                        "phone_number": "",
                        "academic_degree": None,
                        "date_of_birth": None,
                        "library": None,
                        "reading_room": None,
                        "readingroombookuser_set": []
                    }
                ]
            }
        }
    ),
}
