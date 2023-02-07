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
    }
)

USERS_RESPONSES_GET = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {
                "User": [
                    {
                        "id": 3,
                        "username": "erin1",
                        "email": "",
                        "last_name": "Solstice",
                        "first_name": "Erin",
                        "middle_name": "",
                        "serial_number": "7701397000",
                        "passport": "0000000000",
                        "address": "Motherland",
                        "education_level": "",
                        "phone_number": "",
                        "academic_degree": "Bachelor's Degree",
                        "date_of_birth": "1995-01-01",
                        "library": {
                            "id": 1,
                            "name": "Liby"
                        },
                        "reading_room": {
                            "id": 1,
                            "name": "Roomy",
                            "capacity": 1,
                            "library": {
                                "id": 1,
                                "name": "Liby"
                            }
                        },
                        "readingroombookuser_set": []
                    }
                ]
            }
        }
    )
}

USER_RESPONSES_GET = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {
                "User": {
                    "id": 3,
                    "username": "erin1",
                    "email": "",
                    "last_name": "Solstice",
                    "first_name": "Erin",
                    "middle_name": "",
                    "serial_number": "7701397000",
                    "passport": "0000000000",
                    "address": "Motherland",
                    "education_level": "",
                    "phone_number": "",
                    "academic_degree": "Bachelor's Degree",
                    "date_of_birth": "1995-01-01",
                    "library": {
                        "id": 1,
                        "name": "Liby"
                    },
                    "reading_room": {
                        "id": 1,
                        "name": "Roomy",
                        "capacity": 1,
                        "library": {
                                "id": 1,
                                "name": "Liby"
                        }
                    },
                    "readingroombookuser_set": []
                }
            }
        }
    )
}

USER_RESPONSES_DELETE = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {
                "Success": "User 'test2' deleted succesfully."
            }
        }
    )
}
USER_RESPONSES_PATCH = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {
                "Success": "User 'latest_Test' updated succesfully."
            }
        }
    )
}


LIBRARIES_RESPONSES_GET = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {
                "Library": [
                    {
                        "id": 1,
                        "name": "Liby",
                        "readingroom_set": [
                            {
                                "id": 1,
                                "name": "Roomy",
                                "capacity": 1,
                                "library": {
                                    "id": 1,
                                    "name": "Liby"
                                }
                            },
                            {
                                "id": 6,
                                "name": "Roomy2",
                                "capacity": 20,
                                "library": {
                                    "id": 1,
                                    "name": "Liby"
                                }
                            }
                        ],
                        "user_set": []
                    }
                ]
            }
        }
    )
}

LIBRARY_RESPONSES_GET = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {
                "Library": {
                    "id": 1,
                    "name": "Liby",
                    "readingroom_set": [
                        {
                            "id": 1,
                            "name": "Roomy",
                            "capacity": 1,
                            "library": {
                                "id": 1,
                                "name": "Liby"
                            }
                        },
                        {
                            "id": 6,
                            "name": "Roomy2",
                            "capacity": 20,
                            "library": {
                                "id": 1,
                                "name": "Liby"
                            }
                        }
                    ],
                    "user_set": []
                }
            }
        }
    )
}

LIBRARY_RESPONSES_DELETE = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {
                "Success": "Library 'Liby' deleted succesfully."
            }
        }
    )
}
LIBRARY_RESPONSES_PATCH = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {
                "Success": "Library 'Liby' updated succesfully."
            }
        }
    )
}


READING_ROOMS_RESPONSES_GET = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {
                "ReadingRoom": [
                    {
                        "id": 1,
                        "name": "Roomy",
                        "capacity": 1,
                        "library": 1
                    },
                    {
                        "id": 6,
                        "name": "Roomy2",
                        "capacity": 20,
                        "library": 1
                    }
                ]
            }
        }
    )
}

READING_ROOM_RESPONSES_GET = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {
                "ReadingRoom": {
                    "id": 6,
                    "name": "Roomy2",
                    "capacity": 20,
                    "library": 1
                }
            }
        }
    )
}

READING_ROOM_RESPONSES_DELETE = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {
                "Success": "ReadingRoom 'Roomy2' deleted succesfully."
            }
        }
    )
}
READING_ROOM_RESPONSES_PATCH = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {
                "Success": "ReadingRoom 'Roomy2' updated succesfully."
            }
        }
    )
}


BOOKS_RESPONSES_GET = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {
                "Book": [
                    {
                        "id": 1,
                        "title": "Booky",
                        "authors": "",
                        "publisher": "",
                        "pub_date": None,
                        "series": "",
                        "total_stock": 21,
                        "isbn": "",
                        "reading_rooms": [
                            1
                        ]
                    },
                    {
                        "id": 2,
                        "title": "Brand new book",
                        "authors": "",
                        "publisher": "",
                        "pub_date": None,
                        "series": "",
                        "total_stock": 5,
                        "isbn": "",
                        "reading_rooms": [
                            1,
                            6
                        ]
                    },
                    {
                        "id": 3,
                        "title": "Rare Book",
                        "authors": "",
                        "publisher": "",
                        "pub_date": None,
                        "series": "",
                        "total_stock": 2,
                        "isbn": "",
                        "reading_rooms": [
                            1
                        ]
                    },
                ]

            }
        }
    )
}

BOOK_RESPONSES_GET = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {
                "Book": {
                    "id": 1,
                    "title": "Booky",
                    "authors": "",
                    "publisher": "",
                    "pub_date": None,
                    "series": "",
                    "total_stock": 21,
                    "isbn": "",
                    "reading_rooms": [
                        1
                    ]
                }
            }
        }
    )
}

BOOK_RESPONSES_DELETE = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {
                "Success": "Book 'Booky' deleted succesfully."
            }
        }
    )
}
BOOK_RESPONSES_PATCH = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {
                "Success": "Book 'Booky' updated succesfully."
            }
        }
    )
}


READING_ROOM_BOOKS_RESPONSES_GET = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {
                "ReadingRoomBook": [
                    {
                        "id": 1,
                        "stock": 20,
                        "book": 1,
                        "reading_room": 1,
                        "borrowers": []
                    },
                    {
                        "id": 6,
                        "stock": 4,
                        "book": 2,
                        "reading_room": 1,
                        "borrowers": []
                    },
                    {
                        "id": 7,
                        "stock": 1,
                        "book": 2,
                        "reading_room": 6,
                        "borrowers": []
                    },
                    {
                        "id": 8,
                        "stock": 2,
                        "book": 3,
                        "reading_room": 1,
                        "borrowers": []
                    }
                ]
            }
        }
    )
}

READING_ROOM_BOOK_RESPONSES_GET = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {
                "ReadingRoomBook": {
                    "id": 1,
                    "stock": 20,
                    "book": 1,
                    "reading_room": 1,
                    "borrowers": []
                }
            }
        }
    )
}


READING_ROOM_BOOK_RESPONSES_DELETE = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {
                "Success": "ReadingRoomBook 'Booky (21 in library) | Roomy (20 in room)' deleted succesfully."
            }
        }
    )
}
READING_ROOM_BOOK_RESPONSES_PATCH = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {
                "Success": "ReadingRoomBook 'Booky (21 in library) | Roomy (20 in room)' updated succesfully."
            }
        }
    )
}

READING_ROOM_BOOK_USERS_RESPONSES_GET = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {}
        }
    )
}

TODO = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {}
        }
    )
}

TODO = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {}
        }
    )
}

TODO = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {}
        }
    )
}

TODO = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {}
        }
    )
}

TODO = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {}
        }
    )
}

TODO = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {}
        }
    )
}

TODO = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {}
        }
    )
}

TODO = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {}
        }
    )
}

TODO = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {}
        }
    )
}
