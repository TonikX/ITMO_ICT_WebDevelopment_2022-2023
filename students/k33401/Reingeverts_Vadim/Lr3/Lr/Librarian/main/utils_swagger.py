from drf_yasg import openapi

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
            "application/json": {
                "ReadingRoomBookUser": [
                    {
                        "id": 16,
                        "borrow_date": "2023-02-07",
                        "returned_date": None,
                        "reading_room_book": 1,
                        "user": 21
                    }
                ]
            }
        }
    )
}


READING_ROOM_BOOK_USER_RESPONSES_GET = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {
                "ReadingRoomBookUser": {
                    "id": 16,
                    "borrow_date": "2023-02-07",
                    "returned_date": None,
                    "reading_room_book": 1,
                    "user": 21
                }
            }
        }
    )
}

READING_ROOM_BOOK_USER_RESPONSES_DELETE = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {
                "Success": "ReadingRoomBookUser 'user | Booky (21 in library) | Roomy (20 in room)' deleted succesfully."
            }
        }
    )
}

READING_ROOM_BOOK_USER_RESPONSES_PATCH = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {
                "Success": "ReadingRoomBookUser 'user | Booky (21 in library) | Roomy (20 in room)' updated succesfully."
            }
        }
    )
}


USER_BOOKS_RESPONSES_GET = {
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
                    }
                ]
            }
        }
    )
}

USERS_BOOKS_OVERDUE_RESPONSES_GET = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {
                "User": [
                    {
                        "id": 15,
                        "username": "admin",
                        "email": "",
                        "last_name": "",
                        "first_name": "",
                        "middle_name": "",
                        "serial_number": "",
                        "passport": "",
                        "address": "",
                        "education_level": "",
                        "phone_number": "",
                        "academic_degree": None,
                        "date_of_birth": None,
                        "library": None,
                        "reading_room": None,
                        "readingroombookuser_set": []
                    },
                    {
                        "id": 21,
                        "username": "user",
                        "email": "",
                        "last_name": "",
                        "first_name": "",
                        "middle_name": "",
                        "serial_number": "1234",
                        "passport": "",
                        "address": "",
                        "education_level": "",
                        "phone_number": "",
                        "academic_degree": None,
                        "date_of_birth": None,
                        "library": None,
                        "reading_room": None,
                        "readingroombookuser_set": [
                            {
                                "id": 16,
                                "borrow_date": "2023-02-07",
                                "returned_date": None,
                                "reading_room_book": {
                                    "id": 1,
                                    "stock": 20,
                                    "book": 1,
                                    "reading_room": 1,
                                    "borrowers": [
                                        21
                                    ]
                                },
                                "user": {
                                    "id": 21,
                                    "password": "pbkdf2_sha256$390000$vRfjjTfuWqF2rzX6ARRQfc$weM9Fs1+F/MpUPNG7y/bEDkvNFwX0jwW7Hp2G2p+HZk=",
                                    "last_login": "2023-02-07T13:53:54.968284Z",
                                    "is_superuser": False,
                                    "username": "user",
                                    "email": "",
                                    "is_staff": False,
                                    "is_active": True,
                                    "date_joined": "2023-02-07T13:44:41Z",
                                    "last_name": "",
                                    "first_name": "",
                                    "middle_name": "",
                                    "serial_number": "1234",
                                    "passport": "",
                                    "address": "",
                                    "education_level": "",
                                    "phone_number": "",
                                    "date_of_birth": None,
                                    "academic_degree": None,
                                    "library": None,
                                    "reading_room": None,
                                    "groups": [],
                                    "user_permissions": []
                                }
                            },
                            {
                                "id": 17,
                                "borrow_date": "2023-01-21",
                                "returned_date": "2023-02-07",
                                "reading_room_book": {
                                    "id": 6,
                                    "stock": 4,
                                    "book": 2,
                                    "reading_room": 1,
                                    "borrowers": [
                                        21
                                    ]
                                },
                                "user": {
                                    "id": 21,
                                    "password": "pbkdf2_sha256$390000$vRfjjTfuWqF2rzX6ARRQfc$weM9Fs1+F/MpUPNG7y/bEDkvNFwX0jwW7Hp2G2p+HZk=",
                                    "last_login": "2023-02-07T13:53:54.968284Z",
                                    "is_superuser": False,
                                    "username": "user",
                                    "email": "",
                                    "is_staff": False,
                                    "is_active": True,
                                    "date_joined": "2023-02-07T13:44:41Z",
                                    "last_name": "",
                                    "first_name": "",
                                    "middle_name": "",
                                    "serial_number": "1234",
                                    "passport": "",
                                    "address": "",
                                    "education_level": "",
                                    "phone_number": "",
                                    "date_of_birth": None,
                                    "academic_degree": None,
                                    "library": None,
                                    "reading_room": None,
                                    "groups": [],
                                    "user_permissions": []
                                }
                            },
                            {
                                "id": 18,
                                "borrow_date": "2019-02-07",
                                "returned_date": None,
                                "reading_room_book": {
                                    "id": 8,
                                    "stock": 2,
                                    "book": 3,
                                    "reading_room": 1,
                                    "borrowers": [
                                        21
                                    ]
                                },
                                "user": {
                                    "id": 21,
                                    "password": "pbkdf2_sha256$390000$vRfjjTfuWqF2rzX6ARRQfc$weM9Fs1+F/MpUPNG7y/bEDkvNFwX0jwW7Hp2G2p+HZk=",
                                    "last_login": "2023-02-07T13:53:54.968284Z",
                                    "is_superuser": False,
                                    "username": "user",
                                    "email": "",
                                    "is_staff": False,
                                    "is_active": True,
                                    "date_joined": "2023-02-07T13:44:41Z",
                                    "last_name": "",
                                    "first_name": "",
                                    "middle_name": "",
                                    "serial_number": "1234",
                                    "passport": "",
                                    "address": "",
                                    "education_level": "",
                                    "phone_number": "",
                                    "date_of_birth": None,
                                    "academic_degree": None,
                                    "library": None,
                                    "reading_room": None,
                                    "groups": [],
                                    "user_permissions": []
                                }
                            }
                        ]
                    }
                ]
            }
        }
    )
}

USERS_BOOKS_RARE_RESPONSES_GET = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {
                "User": [
                    {
                        "id": 21,
                        "username": "user",
                        "email": "",
                        "last_name": "",
                        "first_name": "",
                        "middle_name": "",
                        "serial_number": "1234",
                        "passport": "",
                        "address": "",
                        "education_level": "",
                        "phone_number": "",
                        "academic_degree": None,
                        "date_of_birth": None,
                        "library": None,
                        "reading_room": None,
                        "readingroombookuser_set": [
                            {
                                "id": 16,
                                "borrow_date": "2023-02-07",
                                "returned_date": None,
                                "reading_room_book": {
                                    "id": 1,
                                    "stock": 20,
                                    "book": 1,
                                    "reading_room": 1,
                                    "borrowers": [
                                        21
                                    ]
                                },
                                "user": {
                                    "id": 21,
                                    "password": "pbkdf2_sha256$390000$vRfjjTfuWqF2rzX6ARRQfc$weM9Fs1+F/MpUPNG7y/bEDkvNFwX0jwW7Hp2G2p+HZk=",
                                    "last_login": "2023-02-07T13:53:54.968284Z",
                                    "is_superuser": False,
                                    "username": "user",
                                    "email": "",
                                    "is_staff": False,
                                    "is_active": True,
                                    "date_joined": "2023-02-07T13:44:41Z",
                                    "last_name": "",
                                    "first_name": "",
                                    "middle_name": "",
                                    "serial_number": "1234",
                                    "passport": "",
                                    "address": "",
                                    "education_level": "",
                                    "phone_number": "",
                                    "date_of_birth": None,
                                    "academic_degree": None,
                                    "library": None,
                                    "reading_room": None,
                                    "groups": [],
                                    "user_permissions": []
                                }
                            },
                            {
                                "id": 17,
                                "borrow_date": "2023-01-21",
                                "returned_date": "2023-02-07",
                                "reading_room_book": {
                                    "id": 6,
                                    "stock": 4,
                                    "book": 2,
                                    "reading_room": 1,
                                    "borrowers": [
                                        21
                                    ]
                                },
                                "user": {
                                    "id": 21,
                                    "password": "pbkdf2_sha256$390000$vRfjjTfuWqF2rzX6ARRQfc$weM9Fs1+F/MpUPNG7y/bEDkvNFwX0jwW7Hp2G2p+HZk=",
                                    "last_login": "2023-02-07T13:53:54.968284Z",
                                    "is_superuser": False,
                                    "username": "user",
                                    "email": "",
                                    "is_staff": False,
                                    "is_active": True,
                                    "date_joined": "2023-02-07T13:44:41Z",
                                    "last_name": "",
                                    "first_name": "",
                                    "middle_name": "",
                                    "serial_number": "1234",
                                    "passport": "",
                                    "address": "",
                                    "education_level": "",
                                    "phone_number": "",
                                    "date_of_birth": None,
                                    "academic_degree": None,
                                    "library": None,
                                    "reading_room": None,
                                    "groups": [],
                                    "user_permissions": []
                                }
                            },
                            {
                                "id": 18,
                                "borrow_date": "2019-02-07",
                                "returned_date": None,
                                "reading_room_book": {
                                    "id": 8,
                                    "stock": 2,
                                    "book": 3,
                                    "reading_room": 1,
                                    "borrowers": [
                                        21
                                    ]
                                },
                                "user": {
                                    "id": 21,
                                    "password": "pbkdf2_sha256$390000$vRfjjTfuWqF2rzX6ARRQfc$weM9Fs1+F/MpUPNG7y/bEDkvNFwX0jwW7Hp2G2p+HZk=",
                                    "last_login": "2023-02-07T13:53:54.968284Z",
                                    "is_superuser": False,
                                    "username": "user",
                                    "email": "",
                                    "is_staff": False,
                                    "is_active": True,
                                    "date_joined": "2023-02-07T13:44:41Z",
                                    "last_name": "",
                                    "first_name": "",
                                    "middle_name": "",
                                    "serial_number": "1234",
                                    "passport": "",
                                    "address": "",
                                    "education_level": "",
                                    "phone_number": "",
                                    "date_of_birth": None,
                                    "academic_degree": None,
                                    "library": None,
                                    "reading_room": None,
                                    "groups": [],
                                    "user_permissions": []
                                }
                            }
                        ]
                    }
                ]
            }
        }
    )
}

USERS_YOUNG_RESPONSES_GET = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {
                "User": [
                    {
                        "id": 22,
                        "username": "young_user",
                        "email": "",
                        "last_name": "",
                        "first_name": "",
                        "middle_name": "",
                        "serial_number": "2601697000",
                        "passport": "",
                        "address": "",
                        "education_level": "",
                        "phone_number": "",
                        "academic_degree": None,
                        "date_of_birth": "2006-01-01",
                        "library": {
                            "id": 1,
                            "name": "Liby"
                        },
                        "reading_room": {
                            "id": 6,
                            "name": "Roomy2",
                            "capacity": 20,
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

USERS_GROUPED_BY_DEGREE_RESPONSES_GET = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {
                "MonthlyReport": {
                    "NewUsersLibrary": {
                        "library": {
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
                            "user_set": [
                                {
                                    "id": 22,
                                    "password": "pbkdf2_sha256$390000$06BlzSMcQPOsLQXanJwZcl$arkMI41HLMl/bimu3GA3BqBVSdTSGwPVHua93jNA1ZY=",
                                    "last_login": None,
                                    "is_superuser": False,
                                    "username": "young_user",
                                    "email": "",
                                    "is_staff": False,
                                    "is_active": True,
                                    "date_joined": "2023-02-07T15:13:06Z",
                                    "last_name": "",
                                    "first_name": "",
                                    "middle_name": "",
                                    "serial_number": "2601697000",
                                    "passport": "",
                                    "address": "",
                                    "education_level": "",
                                    "phone_number": "",
                                    "date_of_birth": "2006-01-01",
                                    "academic_degree": None,
                                    "library": {
                                        "id": 1,
                                        "name": "Liby"
                                    },
                                    "reading_room": {
                                        "id": 6,
                                        "name": "Roomy2",
                                        "capacity": 20,
                                        "library": {
                                            "id": 1,
                                            "name": "Liby"
                                        }
                                    },
                                    "groups": [],
                                    "user_permissions": []
                                }
                            ]
                        },
                        "dates": {
                            "2023-02-07": [
                                {
                                    "id": 22,
                                    "username": "young_user",
                                    "email": "",
                                    "last_name": "",
                                    "first_name": "",
                                    "middle_name": "",
                                    "serial_number": "2601697000",
                                    "passport": "",
                                    "address": "",
                                    "education_level": "",
                                    "phone_number": "",
                                    "academic_degree": None,
                                    "date_of_birth": "2006-01-01",
                                    "library": {
                                        "id": 1,
                                        "name": "Liby"
                                    },
                                    "reading_room": {
                                        "id": 6,
                                        "name": "Roomy2",
                                        "capacity": 20,
                                        "library": {
                                            "id": 1,
                                            "name": "Liby"
                                        }
                                    },
                                    "readingroombookuser_set": []
                                }
                            ]
                        }
                    },
                    "NewUsersReadingRooms": [
                        {
                            "reading_room": {
                                "id": 1,
                                "name": "Roomy",
                                "capacity": 1,
                                "library": 1
                            },
                            "dates": {}
                        },
                        {
                            "reading_room": {
                                "id": 6,
                                "name": "Roomy2",
                                "capacity": 20,
                                "library": 1
                            },
                            "dates": {
                                "2023-02-07": [
                                    {
                                        "id": 22,
                                        "username": "young_user",
                                        "email": "",
                                        "last_name": "",
                                        "first_name": "",
                                        "middle_name": "",
                                        "serial_number": "2601697000",
                                        "passport": "",
                                        "address": "",
                                        "education_level": "",
                                        "phone_number": "",
                                        "academic_degree": None,
                                        "date_of_birth": "2006-01-01",
                                        "library": {
                                            "id": 1,
                                            "name": "Liby"
                                        },
                                        "reading_room": {
                                            "id": 6,
                                            "name": "Roomy2",
                                            "capacity": 20,
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
                    ]
                }
            }
        }
    )
}

REPORT_RESPONSES_GET = {
    "200": openapi.Response(
        description="Click 'Example Value' to load response",
        examples={
            "application/json": {
                "MonthlyReport": {
                    "NewUsersLibrary": {
                        "library": {
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
                            "user_set": [
                                {
                                    "id": 22,
                                    "password": "pbkdf2_sha256$390000$06BlzSMcQPOsLQXanJwZcl$arkMI41HLMl/bimu3GA3BqBVSdTSGwPVHua93jNA1ZY=",
                                    "last_login": None,
                                    "is_superuser": False,
                                    "username": "young_user",
                                    "email": "",
                                    "is_staff": False,
                                    "is_active": True,
                                    "date_joined": "2023-02-07T15:13:06Z",
                                    "last_name": "",
                                    "first_name": "",
                                    "middle_name": "",
                                    "serial_number": "2601697000",
                                    "passport": "",
                                    "address": "",
                                    "education_level": "",
                                    "phone_number": "",
                                    "date_of_birth": "2006-01-01",
                                    "academic_degree": None,
                                    "library": {
                                        "id": 1,
                                        "name": "Liby"
                                    },
                                    "reading_room": {
                                        "id": 6,
                                        "name": "Roomy2",
                                        "capacity": 20,
                                        "library": {
                                            "id": 1,
                                            "name": "Liby"
                                        }
                                    },
                                    "groups": [],
                                    "user_permissions": []
                                }
                            ]
                        },
                        "dates": {
                            "2023-02-07": [
                                {
                                    "id": 22,
                                    "username": "young_user",
                                    "email": "",
                                    "last_name": "",
                                    "first_name": "",
                                    "middle_name": "",
                                    "serial_number": "2601697000",
                                    "passport": "",
                                    "address": "",
                                    "education_level": "",
                                    "phone_number": "",
                                    "academic_degree": None,
                                    "date_of_birth": "2006-01-01",
                                    "library": {
                                        "id": 1,
                                        "name": "Liby"
                                    },
                                    "reading_room": {
                                        "id": 6,
                                        "name": "Roomy2",
                                        "capacity": 20,
                                        "library": {
                                            "id": 1,
                                            "name": "Liby"
                                        }
                                    },
                                    "readingroombookuser_set": []
                                }
                            ]
                        }
                    },
                    "NewUsersReadingRooms": [
                        {
                            "reading_room": {
                                "id": 1,
                                "name": "Roomy",
                                "capacity": 1,
                                "library": 1
                            },
                            "dates": {}
                        },
                        {
                            "reading_room": {
                                "id": 6,
                                "name": "Roomy2",
                                "capacity": 20,
                                "library": 1
                            },
                            "dates": {
                                "2023-02-07": [
                                    {
                                        "id": 22,
                                        "username": "young_user",
                                        "email": "",
                                        "last_name": "",
                                        "first_name": "",
                                        "middle_name": "",
                                        "serial_number": "2601697000",
                                        "passport": "",
                                        "address": "",
                                        "education_level": "",
                                        "phone_number": "",
                                        "academic_degree": None,
                                        "date_of_birth": "2006-01-01",
                                        "library": {
                                            "id": 1,
                                            "name": "Liby"
                                        },
                                        "reading_room": {
                                            "id": 6,
                                            "name": "Roomy2",
                                            "capacity": 20,
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
                    ]
                }
            }
        }
    )
}
