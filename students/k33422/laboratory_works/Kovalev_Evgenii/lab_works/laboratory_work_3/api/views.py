from collections import defaultdict
from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.db.models import F, Count, Sum, Q
from django.db.models.functions import Extract, Now
from rest_framework import generics, serializers, permissions, mixins
from rest_framework.generics import get_object_or_404, RetrieveUpdateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.permissions import IsLibraryWorker
from api.serializers import *
from library_app.models import *


class CreateUserView:
    model = User


class CreateReaderView(CreateUserView, generics.CreateAPIView):
    serializer_class = ReaderSerializer


class CreateAuthorView(CreateUserView, generics.CreateAPIView):
    serializer_class = AuthorSerializer


class ReaderBooksView(generics.ListAPIView):
    serializer_class = BookCopySerializer
    # имя GET-параметра
    lookup_url_kwarg = 'reader'

    def get_queryset(self):
        author_name = self.request.query_params.get(self.lookup_url_kwarg)
        author = get_object_or_404(User, username=author_name)
        return BookCopy.objects.filter(reader=author)


class MonthAgoReadersView(generics.ListAPIView):
    serializer_class = ReaderSerializer

    def get_queryset(self):
        # определеяем книги, взятые месяц и более назад
        books = BookCopy.objects.filter(own_date__lte=(datetime.now().date() - relativedelta(months=1)))
        return [book_copy.reader for book_copy in books]  # if book_copy.reader.role == User.READER]


class RareBooksReadersView(generics.ListAPIView):
    serializer_class = ReaderSerializer

    def get_queryset(self):
        # группировка по полю book
        books = [
            book['book'] for book in
            BookCopy.objects.values('book').annotate(count=Count('*')).filter(count__lte=2)
        ]

        # конвертируем в множество, чтобы избавиться от дублирующихся читателей
        return set(book.reader for book in BookCopy.objects.filter(book__in=books))


class ReadersUnder20View(generics.ListAPIView):
    serializer_class = ReaderSerializer

    def get_queryset(self):
        return User.objects.filter(
            Q(library_card_number__isnull=False)
            &
            Q(birth_date__gte=(datetime.now().date() - relativedelta(years=20)))
        )


class ReadersEducationStatsView(APIView):
    @staticmethod
    def __calc_and_format_result(specific_count, all_count):
        return f'{round(specific_count / all_count * 100, 2)}%'

    def get(self, request):
        users_count = User.objects.count()
        secondary_education_percent = User.objects.filter(education=User.SECONDARY).count()
        high_education_percent = User.objects.filter(education=User.HIGH).count()
        degree_percent = User.objects.filter(is_have_degree=True).count()

        return Response({
            'secondary_education_percent': self.__calc_and_format_result(secondary_education_percent, users_count),
            'high_education_percent': self.__calc_and_format_result(high_education_percent, users_count),
            'degree_percent': self.__calc_and_format_result(degree_percent, users_count),
        })


class RegisterReaderView(generics.UpdateAPIView):
    serializer_class = LibraryWorkerReaderUpdateSerializer
    queryset = User.objects.all()
    permission_classes = [IsLibraryWorker]
    lookup_url_kwarg = 'username'
    lookup_field = 'username'


class ExcludeYearAgoReaders(APIView):
    def post(self, request):
        if request.user.role != User.LIBRARY_WORKER:
            return Response({'detail': "Недостаточно прав (авторизуйтесь под работником библиотеки)"''})

        queryset = User.objects.filter(register_date__lt=(datetime.now().date() - relativedelta(months=12)))
        response = {'detail': [user.username for user in queryset]}
        queryset.delete()
        return Response(response)


class DeleteBookCopyView(APIView):
    def post(self, request, **kwargs):
        if request.user.role != User.LIBRARY_WORKER:
            return Response({'detail': "Недостаточно прав (авторизуйтесь под работником библиотеки)"''})

        cypher = kwargs.get('cypher')
        queryset = BookCopy.objects.filter(book__cypher=cypher)

        get_object_or_404(Book, cypher=cypher)
        response = {'detail': {'book': [str(book_copy) for book_copy in queryset], 'cypher': cypher}}
        queryset.delete()
        Book.objects.get(cypher=cypher).delete()
        return Response(response)


class BookRegisterView(generics.CreateAPIView):
    permission_classes = [IsLibraryWorker]
    serializer_class = BookSerializer


class ReportView(APIView):
    def get(self, request, **kwargs):

        month = request.query_params.get('month')

        if month:
            if int(month) not in range(1, 13):
                return Response({'detail': 'Параметр month должен принимать значение от 1 до 12'})

        readers_for_month = User.objects.filter(
            Q(role=User.READER) &
            Q(library_card_number__isnull=False) &
            Q(register_date__month=month) &
            Q(register_date__year=datetime.today().year)
        )
        # for r in readers_for_month:
        #     print(r)

        reading_rooms_books_info = defaultdict(int)
        reading_rooms_readers_info = defaultdict(int)

        book_copies = BookCopy.objects.all()

        for book_copy in book_copies:
            for room in book_copy.reading_room.all():
                reading_rooms_books_info[str(room)] += 1

                if book_copy.reader:
                    reading_rooms_readers_info[str(room)] += 1

        response = {
            'reading_rooms_books_count_info': {
                reading_room: f'количество книг: {count}' for reading_room, count in reading_rooms_books_info.items()
            },

            'reading_rooms_readers_info': {
                reading_room: f'количество читателей: {count}' for reading_room, count in
                reading_rooms_readers_info.items()
            }
        }

        reading_rooms_readers_count = list(
            User.objects
            .filter(Q(role=User.READER) & Q(register_date__month=month) & Q(register_date__year=datetime.today().year))
            .values('reader_room')
            .annotate(readers_count=Count('*'))
        )

        # пары вида <pk читального зала>: <количество читателей>
        reading_rooms_readers_count_info = {
            obj['reader_room']: obj['readers_count'] for obj in
            reading_rooms_readers_count
        }

        # print(reading_rooms_readers_count_info)
        all_reading_rooms_info = defaultdict(list)

        # словарь вида <название библиотеки>: <список читальных залов (в виде объектов БД) библиотеки>
        for room in ReadingRoom.objects.all():
            all_reading_rooms_info[str(room.library)] += [room]

        # собираем словарь с библиотеками и количеством читателей в читальных залах
        for lib, rooms in all_reading_rooms_info.items():
            rooms_list = []

            for room in rooms:
                # если ключа читального зала нет, значит в зале 0 читателей
                readers_count = reading_rooms_readers_count_info.get(room.pk, 0)
                rooms_list.append({str(room): readers_count})

            all_reading_rooms_info[str(lib)] = rooms_list

        # for lib, rooms in all_reading_rooms_info.items():
        #     print(lib, rooms)

        if month:
            response[f'readers_for_{month}_month_info'] = {
                reading_room: count for reading_room, count in
                all_reading_rooms_info.items()
            }

        return Response(response)
