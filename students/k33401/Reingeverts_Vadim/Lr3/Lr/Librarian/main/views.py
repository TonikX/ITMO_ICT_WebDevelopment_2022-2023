import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from . import models, serializers


class ModelsAPIView(APIView):
    authentication_classes = [SessionAuthentication,
                              BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

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


class ModelDetailsAPIView(APIView):
    model = None
    modelSerializer = None

    def get(self, request, pk, *args, **kwargs):
        object = self.model.objects.get(pk=pk)
        serializer = self.modelSerializer(object)
        return Response({self.model.__name__: serializer.data})

    def delete(self, request, pk, *args, **kwargs):
        object = self.model.objects.get(pk=pk)
        object.delete()
        return Response({"Success": f"{self.model.__name__} '{object}' deleted succesfully."})

    def patch(self, request, pk, *args, **kwargs):
        prev_object = self.model.objects.get(pk=pk)

        object_data = request.data.get(self.model.__name__)
        serializer = self.modelSerializer(
            prev_object, data=object_data, partial=True)

        if serializer.is_valid(raise_exception=True):
            new_object = serializer.save()

        return Response({"Success": f"{self.model.__name__} '{new_object}' updated succesfully."})


class UsersAPIView(ModelsAPIView):
    model = models.User
    modelSerializer = serializers.UserSerializer


class UserDetailsAPIView(ModelDetailsAPIView):
    model = models.User
    modelSerializer = serializers.UserSerializer


class LibrariesAPIView(ModelsAPIView):
    model = models.Library
    modelSerializer = serializers.LibrarySerializer


class LibraryDetailsAPIView(ModelDetailsAPIView):
    model = models.Library
    modelSerializer = serializers.LibrarySerializer


class ReadingRoomsAPIView(ModelsAPIView):
    model = models.ReadingRoom
    modelSerializer = serializers.ReadingRoomSerializer


class ReadingRoomDetailsAPIView(ModelDetailsAPIView):
    model = models.ReadingRoom
    modelSerializer = serializers.ReadingRoomSerializer


class BooksAPIView(ModelsAPIView):
    model = models.Book
    modelSerializer = serializers.BookSerializer


class BookDetailsAPIView(ModelDetailsAPIView):
    model = models.Book
    modelSerializer = serializers.BookSerializer


class ReadingRoomBooksAPIView(ModelsAPIView):
    model = models.ReadingRoomBook
    modelSerializer = serializers.ReadingRoomBookSerializer


class ReadingRoomBookDetailsAPIView(ModelDetailsAPIView):
    model = models.ReadingRoomBook
    modelSerializer = serializers.ReadingRoomBookSerializer


class ReadingRoomBookUsersAPIView(ModelsAPIView):
    model = models.ReadingRoomBookUser
    modelSerializer = serializers.ReadingRoomBookUserSerializer


class ReadingRoomBookUserDetailsAPIView(ModelDetailsAPIView):
    model = models.ReadingRoomBookUser
    modelSerializer = serializers.ReadingRoomBookUserSerializer


# "Какие книги закреплены за заданным читателем?"
class UserBooksAPIView(APIView):
    model = models.User
    modelSerializer = serializers.UserSerializer

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


# "Кто из читателей взял книгу более месяца тому назад?"
class UsersYoungAPIView(APIView):
    model = models.User
    modelSerializer = serializers.UserSerializer

    def get(self, request, *args, **kwargs):
        now = datetime.datetime.now()
        month_ago = now - datetime.timedelta(days=30)

        objects = self.model.objects.filter(
            readingroombookuser__borrow_date__lte=month_ago, readingroombookuser__returned_date__isnull=True)
        serializer = self.modelSerializer(objects, many=True)

        return Response({self.model.__name__: serializer.data})


# За кем из читателей закреплены книги, количество экземпляров которых в библиотеке не превышает 2?
class UsersBooksRareAPIView(APIView):
    model = models.User
    modelSerializer = serializers.UserSerializer

    def get(self, request, *args, **kwargs):
        objects = self.model.objects.filter(
            readingroombookuser__reading_room_book__book__total_stock__lte=2, readingroombookuser__returned_date__isnull=True)
        serializer = self.modelSerializer(objects, many=True)

        return Response({self.model.__name__: serializer.data})


# Сколько в библиотеке читателей младше 20 лет?
class UsersYoungAPIView(APIView):
    model = models.User
    modelSerializer = serializers.UserSerializer

    def get(self, request, *args, **kwargs):
        now = datetime.datetime.now()
        twenty_years_ago = now - datetime.timedelta(days=20 * 365)

        objects = self.model.objects.filter(
            date_of_birth__lte=twenty_years_ago)
        serializer = self.modelSerializer(objects, many=True)

        return Response({self.model.__name__: serializer.data})


# Сколько читателей в процентном отношении имеют начальное образование, среднее, высшее, ученую степень?
class UsersGroupedByDegreeAPIView(APIView):
    model = models.User
    modelSerializer = serializers.UserSerializer

    def get(self, request, *args, **kwargs):
        degrees_dict = self.model.group_by_degree()

        degree_data = {}
        for degree, user in degrees_dict.items():
            serializer = self.modelSerializer(user, many=True)
            degree_data[degree] = serializer.data

        return Response({"Degree": degree_data})


# Необходимо предусмотреть возможность выдачи отчета о работе библиотеки в течение месяца.
# Отчет должен включать в себя следующую информацию:
# - количество книг читателей на каждый день в каждом из залов и в библиотеке в целом
# - количество читателей, записавшихся в библиотеку в каждый зал и в библиотеку за отчетный месяц.
class LibraryMonthlyReportAPIView(APIView):
    model = models.Library
    modelSerializer = serializers.LibrarySerializer
    userSerializer = serializers.UserSerializer
    readingRoomSerializer = serializers.ReadingRoomSerializer

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
