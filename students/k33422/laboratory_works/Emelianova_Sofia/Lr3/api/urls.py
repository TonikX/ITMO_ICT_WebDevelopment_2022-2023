from django.urls import path, include, re_path
from rest_framework_swagger.views import get_swagger_view

from api.views import *

API_PREFIX = 'api/v1'

urlpatterns = [
    # маршруты для работы аутентификации на базе обычных токенов
    # для авторизации в Postman нужно добавить заголовок Authorization со значением "Token <token>"
    # токен генерируется на странице http://127.0.0.1:8000/auth/token/login
    # также для генерации токена на адрес выше можно отправить post-запрос:
    # {
    #     "username": "admin",
    #     "password": "admin","
    # }

    path(f'{API_PREFIX}/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    # ------------------------ ENDPOINTS ------------------------

    # АВТОРИЗАЦИЯ ОСУЩЕСТВЛЯЕТСЯ ДОБАВЛЕНИЕМ ЗАГОЛОВКА Authorization
    # ПРИМЕР: Authorization: Token 86dac6a02a74f0b61d61a8a4d939230994061c49

    # Регистрация читателя в общем смысле (можно зарегаться как в системе, так и в библиотеке)
    # Регистрация в библиотеке интерпретируется как присвоение читателю library_card_number
    # С пустым library_card_number читатель считается незарегистрированным в библиотеке
    # URL: http://127.0.0.1:8000/api/v1/reader-register/
    # METHOD: POST
    # BODY EXAMPLE:
    #     {
    #         "username": "reader2",
    #         "password": "reader",
    #         "phone": "892342511",
    #         "library_card_number": "2345",
    #         "education": 1,
    #         "reader_room": 1,
    #         "is_have_degree": True,
    #     }
    path(f'{API_PREFIX}/reader-register/', CreateReaderView.as_view()),
    path(f'{API_PREFIX}/author-register/', CreateAuthorView.as_view()),

    # Книги определенного читателя (http://127.0.0.1:8000/api/v1/books/?reader=admin)
    path(f'{API_PREFIX}/books/', ReaderBooksView.as_view()),

    # Читатели, взявшие книгу более месяца назад
    path(f'{API_PREFIX}/month-ago-readers/', MonthAgoReadersView.as_view()),

    # Читатели, взявшие книги, количество экземпляров которых не превышает 2
    path(f'{API_PREFIX}/rare-books-readers/', RareBooksReadersView.as_view()),

    # Читатели младше 20 лет
    path(f'{API_PREFIX}/readers-under-20/', ReadersUnder20View.as_view()),

    # Читатели в процентном распределении по критерию образования
    path(f'{API_PREFIX}/readers-education-stats/', ReadersEducationStatsView.as_view()),

    # Запись читателя в библиотеку (или изменение номера билета и читательского зала)
    # Записать читателя может только пользователь с ролью "Работник библиотеки"
    # Пример:
    # URL: http://127.0.0.1:8000/api/v1/lib-reader-register/admin/
    # METHOD: PATCH/PUT
    # BODY EXAMPLE:
    # {
    #     "library_card_number": "1235666",
    #     "reader_room": 1
    # }
    path(f'{API_PREFIX}/lib-reader-register/<str:username>/', RegisterReaderView.as_view()),

    # Удалить пользователей, зарегистрированных в библиотеке более года назад
    path(f'{API_PREFIX}/drop-year-ago-readers/', ExcludeYearAgoReaders.as_view()),

    # Удаление книги по шифру (POST-запрос)
    path(f'{API_PREFIX}/drop-book-copy-by-cypher/<str:cypher>/', DeleteBookCopyView.as_view()),

    # Принять книгу в фонд библиотеки (POST-запрос)
    # BODY EXAMPLE:
    # {
    #     "title": "Приключения Тома Сойера",
    #     "year": 2001,
    #     "cypher": "ISBNXXX",
    #     "reading_room": [1] (это поле можно убрать)
    # }
    path(f'{API_PREFIX}/book-register/', BookRegisterView.as_view()),

    # Отчет (http://127.0.0.1:8000/api/v1/report/?month=1/)
    path(f'{API_PREFIX}/report/', ReportView.as_view()),

    # Редактирование данных пользователя (PUT method)
    # {
    #     "username": "admins",
    #     "password": "admin",
    #     "phone": "8996"
    # }
    path(f'{API_PREFIX}/user-edit/<str:username>/', EditUserView.as_view()),

    # Взять экземпляр книги (POST method)
    # {
    #     "book": "b1"
    # }
    path(f'{API_PREFIX}/get-book/<str:username>/', GetBookView.as_view()),

    # Вернуть экземпляр книги (POST method)
    # {
    #     "book": "b1"
    # }
    path(f'{API_PREFIX}/return-book/<str:username>/', ReturnBookView.as_view()),

    # Все экземпляры книг (GET method)
    path(f'{API_PREFIX}/books-copies/', BooksCopiesView.as_view()),

    # Получить информацию по пользователю
    path(f'{API_PREFIX}/get-user-info/<str:username>/', GetUserInfoView.as_view())
]
