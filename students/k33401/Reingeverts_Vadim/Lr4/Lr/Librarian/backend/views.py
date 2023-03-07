import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from drf_yasg.utils import swagger_auto_schema

from . import models, serializers, utils_swagger


class BaseModelAPIView(APIView):
    authentication_classes = [SessionAuthentication,
                              BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class ModelsAPIView(BaseModelAPIView):
    model = None
    modelSerializer = None

    def get(self, request, *args, **kwargs):
        objects = self.model.objects.all()
        serializer = self.modelSerializer(objects, many=True)
        return Response({self.model.__name__: serializer.data})

    def post(self, request, *args, **kwargs):
        object_data = request.data.get(self.model.__name__)
        serializer = self.modelSerializer(data=object_data)

        if serializer.is_valid(raise_exception=True):
            new_object = serializer.save()

        return Response({"Success": f"{self.model.__name__} '{new_object}' created succesfully."})


class ModelDetailsAPIView(BaseModelAPIView):
    model = None
    modelSerializer = None

    def get(self, request, pk, *args, **kwargs):
        try:
            object = self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return Response({"Error": f"{self.model.__name__} with id {pk} does not exist."}, 400)

        serializer = self.modelSerializer(object)
        return Response({self.model.__name__: serializer.data})

    def delete(self, request, pk, *args, **kwargs):
        try:
            object = self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return Response({"Error": f"{self.model.__name__} with id {pk} does not exist."}, 400)

        object.delete()
        return Response({"Success": f"{self.model.__name__} '{object}' deleted succesfully."})

    def patch(self, request, pk, *args, **kwargs):
        try:
            prev_object = self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return Response({"Error": f"{self.model.__name__} with id {pk} does not exist."}, 400)

        object_data = request.data.get(self.model.__name__)
        serializer = self.modelSerializer(
            prev_object, data=object_data, partial=True)

        if serializer.is_valid(raise_exception=True):
            new_object = serializer.save()

        return Response({"Success": f"{self.model.__name__} '{new_object}' updated succesfully."})


# All model representations in API view
class UsersAPIView(ModelsAPIView):
    model = models.User
    modelSerializer = serializers.UserSerializer

    @swagger_auto_schema(
        operation_summary="returns users",
        operation_description="List of all user objects",
        tags=['User'],
        responses=utils_swagger.USERS_RESPONSES_GET
    )
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    @swagger_auto_schema(
        operation_summary="adds user",
        operation_description="User to be added to the library",

        request_body=serializers.UserSerializer,
        tags=['User'],
    )
    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)

    def check_permissions(self, request):
        if request.method == 'POST':
            return
        super().check_permissions(request)


class UserDetailsAPIView(ModelDetailsAPIView):
    model = models.User
    modelSerializer = serializers.UserSerializer

    @swagger_auto_schema(
        operation_summary="returns user",
        operation_description="Single user specifed by pk",
        tags=['User'],
        responses=utils_swagger.USER_RESPONSES_GET
    )
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    @swagger_auto_schema(
        operation_summary="deletes user",
        operation_description="Deletes user specifed by pk",
        tags=['User'],
        responses=utils_swagger.USER_RESPONSES_DELETE
    )
    def delete(self, *args, **kwargs):
        return super().delete(*args, **kwargs)

    @swagger_auto_schema(
        operation_summary="updates user",
        operation_description="Updates user specifed by pk",
        request_body=serializers.UserSerializer,
        tags=['User'],
        responses=utils_swagger.USER_RESPONSES_PATCH
    )
    def patch(self, *args, **kwargs):
        return super().patch(*args, **kwargs)


class LibrariesAPIView(ModelsAPIView):
    model = models.Library
    modelSerializer = serializers.LibrarySerializer

    @swagger_auto_schema(
        operation_summary="returns libraries",
        operation_description="List of all library objects",
        tags=['Library'],
        responses=utils_swagger.LIBRARIES_RESPONSES_GET
    )
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    @swagger_auto_schema(
        operation_summary="adds library",
        operation_description="Library to be added to the library",

        request_body=serializers.LibrarySerializer,
        tags=['Library']
    )
    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)


class LibraryDetailsAPIView(ModelDetailsAPIView):
    model = models.Library
    modelSerializer = serializers.LibrarySerializer

    @swagger_auto_schema(
        operation_summary="returns library",
        operation_description="Single library specifed by pk",
        tags=['Library'],
        responses=utils_swagger.LIBRARY_RESPONSES_GET
    )
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    @swagger_auto_schema(
        operation_summary="deletes library",
        operation_description="Deletes library specifed by pk",
        tags=['Library'],
        responses=utils_swagger.LIBRARY_RESPONSES_DELETE
    )
    def delete(self, *args, **kwargs):
        return super().delete(*args, **kwargs)

    @swagger_auto_schema(
        operation_summary="updates library",
        operation_description="Updates library specifed by pk",
        request_body=serializers.LibrarySerializer,
        tags=['Library'],
        responses=utils_swagger.LIBRARY_RESPONSES_PATCH
    )
    def patch(self, *args, **kwargs):
        return super().patch(*args, **kwargs)


class ReadingRoomsAPIView(ModelsAPIView):
    model = models.ReadingRoom
    modelSerializer = serializers.ReadingRoomSerializer

    @swagger_auto_schema(
        operation_summary="returns reading rooms",
        operation_description="List of all reading room objects",
        tags=['Reading Room'],
        responses=utils_swagger.READING_ROOMS_RESPONSES_GET
    )
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    @swagger_auto_schema(
        operation_summary="adds reading room",
        operation_description="Reading room to be added to the library",

        request_body=serializers.LibrarySerializer,
        tags=['Reading Room']
    )
    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)


class ReadingRoomDetailsAPIView(ModelDetailsAPIView):
    model = models.ReadingRoom
    modelSerializer = serializers.ReadingRoomSerializer

    @swagger_auto_schema(
        operation_summary="returns reading room",
        operation_description="Single reading room specifed by pk",
        tags=['Reading Room'],
        responses=utils_swagger.READING_ROOM_RESPONSES_GET
    )
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    @swagger_auto_schema(
        operation_summary="deletes reading room",
        operation_description="Deletes reading room specifed by pk",
        tags=['Reading Room'],
        responses=utils_swagger.READING_ROOM_RESPONSES_DELETE
    )
    def delete(self, *args, **kwargs):
        return super().delete(*args, **kwargs)

    @swagger_auto_schema(
        operation_summary="updates reading room",
        operation_description="Updates reading room specifed by pk",
        request_body=serializers.ReadingRoomSerializer,
        tags=['Reading Room'],
        responses=utils_swagger.READING_ROOM_RESPONSES_PATCH
    )
    def patch(self, *args, **kwargs):
        return super().patch(*args, **kwargs)


class BooksAPIView(ModelsAPIView):
    model = models.Book
    modelSerializer = serializers.BookSerializer

    @swagger_auto_schema(
        operation_summary="returns books",
        operation_description="List of all book objects",
        tags=['Book'],
        responses=utils_swagger.BOOKS_RESPONSES_GET

    )
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    @swagger_auto_schema(
        operation_summary="adds book",
        operation_description="Book to be added to the library",

        request_body=serializers.BookSerializer,
        tags=['Book']
    )
    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)


class BookDetailsAPIView(ModelDetailsAPIView):
    model = models.Book
    modelSerializer = serializers.BookSerializer

    @swagger_auto_schema(
        operation_summary="returns book",
        operation_description="Single book specifed by pk",
        tags=['Book'],
        responses=utils_swagger.BOOK_RESPONSES_GET
    )
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    @swagger_auto_schema(
        operation_summary="deletes book",
        operation_description="Deletes book specifed by pk",
        tags=['Book'],
        responses=utils_swagger.BOOK_RESPONSES_DELETE
    )
    def delete(self, *args, **kwargs):
        return super().delete(*args, **kwargs)

    @swagger_auto_schema(
        operation_summary="updates book",
        operation_description="Updates book specifed by pk",
        request_body=serializers.BookSerializer,
        tags=['Book'],
        responses=utils_swagger.BOOK_RESPONSES_PATCH
    )
    def patch(self, *args, **kwargs):
        return super().patch(*args, **kwargs)


class ReadingRoomBooksAPIView(ModelsAPIView):
    model = models.ReadingRoomBook
    modelSerializer = serializers.ReadingRoomBookSerializer

    @swagger_auto_schema(
        operation_summary="returns reading room books",
        operation_description="List of all reading room book objects",
        tags=['Reading Room Book'],
        responses=utils_swagger.READING_ROOM_BOOKS_RESPONSES_GET
    )
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    @swagger_auto_schema(
        operation_summary="adds reading room book",
        operation_description="Reading room book to be added to the reading room",

        request_body=serializers.ReadingRoomBookSerializer,
        tags=['Reading Room Book']
    )
    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)


class ReadingRoomBookDetailsAPIView(ModelDetailsAPIView):
    model = models.ReadingRoomBook
    modelSerializer = serializers.ReadingRoomBookSerializer

    @swagger_auto_schema(
        operation_summary="returns reading room book",
        operation_description="Single reading room book specifed by pk",
        tags=['Reading Room Book'],
        responses=utils_swagger.READING_ROOM_BOOK_RESPONSES_GET
    )
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    @swagger_auto_schema(
        operation_summary="deletes reading room book",
        operation_description="Deletes reading room book specifed by pk",
        tags=['Reading Room Book'],
        responses=utils_swagger.READING_ROOM_BOOK_RESPONSES_DELETE
    )
    def delete(self, *args, **kwargs):
        return super().delete(*args, **kwargs)

    @swagger_auto_schema(
        operation_summary="updates reading room book",
        operation_description="Updates reading room book specifed by pk",
        request_body=serializers.ReadingRoomBookSerializer,
        tags=['Reading Room Book'],
        responses=utils_swagger.READING_ROOM_BOOK_RESPONSES_PATCH
    )
    def patch(self, *args, **kwargs):
        return super().patch(*args, **kwargs)


class ReadingRoomBookUsersAPIView(ModelsAPIView):
    model = models.ReadingRoomBookUser
    modelSerializer = serializers.ReadingRoomBookUserSerializer

    @swagger_auto_schema(
        operation_summary="returns reading room book users",
        operation_description="List of all reading room book user objects",
        tags=['Reading Room Book User'],
        responses=utils_swagger.READING_ROOM_BOOK_USERS_RESPONSES_GET

    )
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    @swagger_auto_schema(
        operation_summary="adds reading room book user",
        operation_description="Reading room book user to be added to the reading room",

        request_body=serializers.ReadingRoomBookUserSerializer,
        tags=['Reading Room Book User']
    )
    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs)


class ReadingRoomBookUserDetailsAPIView(ModelDetailsAPIView):
    model = models.ReadingRoomBookUser
    modelSerializer = serializers.ReadingRoomBookUserSerializer

    @swagger_auto_schema(
        operation_summary="returns reading room book user",
        operation_description="Single reading room book user specifed by pk",
        tags=['Reading Room Book User'],
        responses=utils_swagger.READING_ROOM_BOOK_USER_RESPONSES_GET
    )
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    @swagger_auto_schema(
        operation_summary="deletes reading room book user",
        operation_description="Deletes reading room book user specifed by pk",
        tags=['Reading Room Book User'],
        responses=utils_swagger.READING_ROOM_BOOK_USER_RESPONSES_DELETE
    )
    def delete(self, *args, **kwargs):
        return super().delete(*args, **kwargs)

    @swagger_auto_schema(
        operation_summary="updates reading room book user",
        operation_description="Updates reading room book user specifed by pk",
        request_body=serializers.ReadingRoomBookUserSerializer,
        tags=['Reading Room Book User'],
        responses=utils_swagger.READING_ROOM_BOOK_USER_RESPONSES_PATCH
    )
    def patch(self, *args, **kwargs):
        return super().patch(*args, **kwargs)


# Custom API views
class UserBooksAPIView(BaseModelAPIView):
    model = models.User
    modelSerializer = serializers.UserSerializer

    @swagger_auto_schema(
        operation_summary="returns books related to the user specifed by pk",
        operation_description="\"Какие книги закреплены за заданным читателем?\"",
        tags=['Custom'],
        responses=utils_swagger.USER_BOOKS_RESPONSES_GET
    )
    def get(self, request, pk, *args, **kwargs):
        object = self.model.objects.get(pk=pk)
        serializer = self.modelSerializer(object)

        try:
            reading_room_book_user_set = serializer.data['readingroombookuser_set']
            books = []
            for reading_room_book_user in reading_room_book_user_set:
                book = reading_room_book_user['reading_room_book']['book']
                books.append(book)
        except KeyError:
            books = []
        return Response({"Book": books})


class UsersBooksOverdueAPIView(BaseModelAPIView):
    model = models.User
    modelSerializer = serializers.UserSerializer

    @swagger_auto_schema(
        operation_summary="returns users who have not returened the book for a month",
        operation_description="\"Кто из читателей взял книгу более месяца тому назад?\"",
        tags=['Custom'],
        responses=utils_swagger.USERS_BOOKS_OVERDUE_RESPONSES_GET
    )
    def get(self, request, *args, **kwargs):
        now = datetime.datetime.now()
        month_ago = now - datetime.timedelta(days=30)

        objects = self.model.objects.filter(
            readingroombookuser__borrow_date__lte=month_ago,
            readingroombookuser__returned_date__isnull=True)
        serializer = self.modelSerializer(objects, many=True)

        return Response({self.model.__name__: serializer.data})


class UsersBooksRareAPIView(BaseModelAPIView):
    model = models.User
    modelSerializer = serializers.UserSerializer

    @swagger_auto_schema(
        operation_summary="returns users who have books which are low in stock (2 or less)",
        operation_description="\"За кем из читателей закреплены книги, количество экземпляров которых в библиотеке не превышает 2?\"",
        tags=['Custom'],
        responses=utils_swagger.USERS_BOOKS_RARE_RESPONSES_GET
    )
    def get(self, request, *args, **kwargs):
        objects = self.model.objects.filter(
            readingroombookuser__reading_room_book__book__total_stock__lte=2, readingroombookuser__returned_date__isnull=True)
        serializer = self.modelSerializer(objects, many=True)

        return Response({self.model.__name__: serializer.data})


class UsersYoungAPIView(BaseModelAPIView):
    model = models.User
    modelSerializer = serializers.UserSerializer

    @swagger_auto_schema(
        operation_summary="returns users who are young (20 y.o. or younger)",
        operation_description="\"Сколько в библиотеке читателей младше 20 лет?\"",
        tags=['Custom'],
        responses=utils_swagger.USERS_YOUNG_RESPONSES_GET
    )
    def get(self, request, *args, **kwargs):
        now = datetime.datetime.now()
        twenty_years_ago = now - datetime.timedelta(days=20 * 365)

        objects = self.model.objects.filter(
            date_of_birth__gte=twenty_years_ago)
        serializer = self.modelSerializer(objects, many=True)

        return Response({self.model.__name__: serializer.data})


class UsersGroupedByDegreeAPIView(BaseModelAPIView):
    model = models.User
    modelSerializer = serializers.UserSerializer

    @swagger_auto_schema(
        operation_summary="returns users grouped by degree",
        operation_description="\"Сколько читателей в процентном отношении имеют начальное образование, среднее, высшее, ученую степень?\"",
        tags=['Custom'],
        responses=utils_swagger.USERS_GROUPED_BY_DEGREE_RESPONSES_GET
    )
    def get(self, request, *args, **kwargs):
        degrees_dict = self.model.group_by_degree()

        degree_data = {}
        for degree, user in degrees_dict.items():
            serializer = self.modelSerializer(user, many=True)
            degree_data[degree] = serializer.data

        return Response({"Degree": degree_data})


class LibraryMonthlyReportAPIView(BaseModelAPIView):
    model = models.Library
    readingRoomSerializer = serializers.ReadingRoomSerializer

    @swagger_auto_schema(
        operation_summary="returns report about new users grouped by day",
        operation_description="""
            \"Необходимо предусмотреть возможность выдачи отчета о работе библиотеки в течение месяца.
            Отчет должен включать в себя следующую информацию:
            - количество книг читателей на каждый день в каждом из залов и в библиотеке в целом
            - количество читателей, записавшихся в библиотеку в каждый зал и в библиотеку за отчетный месяц.\"
        """,
        tags=['Report'],
        responses=utils_swagger.REPORT_RESPONSES_GET
    )
    def get(self, request, pk, year=None, month=None, *args, **kwargs):
        library = self.model.objects.get(pk=pk)
        grouped_library_users = library.group_new_users_by_day(
            year=year, month=month)
        grouped_rooms_users = library.group_new_users_by_day_per_room(
            year=year, month=month)

        grouped_library_serializer = serializers.GroupedLibraryUsersSerializer(
            grouped_library_users)
        grouped_rooms_serializer = serializers.GroupedReadingRoomsUsersSerializer(
            grouped_rooms_users)

        report_data = {
            "NewUsersLibrary": grouped_library_serializer.data,
            "NewUsersReadingRooms": grouped_rooms_serializer.data,
        }
        return Response({"MonthlyReport": report_data})


# class SignupWithSerialAPIView(APIView):
#     authentication_classes = []
#     permission_classes = []

#     model = models.User
#     modelSerializer = serializers.UserSerializer

#     @swagger_auto_schema(
#         operation_summary="creates a new user with serial number prefilled",
#         operation_description="User to be added to the library",

#         request_body=serializers.UserSerializer,
#         tags=['User']
#     )
#     def post(self, request, *args, **kwargs):
#         object_data = request.data.get(self.model.__name__)
#         serializer = self.modelSerializer(data=object_data)

#         if serializer.is_valid(raise_exception=True):
#             new_object = serializer.save()

#         return Response({"Success": f"{self.model.__name__} '{new_object}' created succesfully."})
