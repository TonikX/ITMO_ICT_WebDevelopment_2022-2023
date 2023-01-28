# Web-программирование
## Лабораторная работа №3
Все файлы лабораторной работы находятся в пул реквесте коллеги (ник soffuk)
https://github.com/TonikX/ITMO_ICT_WebDevelopment_2022-2023/pull/39
### Задание: 
Создать программную систему, предназначенную для работников библиотеки. Такая система должна обеспечивать хранение сведений об имеющихся в библиотеке книгах, о читателях библиотеки и читальных залах.

Для каждой книги в БД должны храниться следующие сведения: название книги, автор (ы), издательство, год издания, раздел, число экземпляров этой книги в каждом зале библиотеки, а также шифр книги и дата закрепления книги за читателем. Книги могут перерегистрироваться в другом зале.

Сведения о читателях библиотеки должны включать номер читательского билета, ФИО читателя, номер паспорта, дату рождения, адрес, номер телефона, образование, наличие ученой степени.

Читатели закрепляются за определенным залом, могут переписаться в другой зал и могут записываться и выписываться из библиотеки.

Библиотека имеет несколько читальных залов, которые характеризуются номером, названием и вместимостью, то есть количеством людей, которые могут одновременно работать в зале.

Библиотека может получать новые книги и списывать старые. Шифр книги может измениться в результате переклассификации, а номер читательского билета в результате перерегистрации.

### Основные файлы с кодом
- models.py

``` py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):

    # https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html
    READER = 1
    AUTHOR = 2
    LIBRARY_WORKER = 3

    ROLE_CHOICES = [
        (READER, 'Читатель'),
        (AUTHOR, 'Автор'),
        (LIBRARY_WORKER, 'Работник библиотеки')
    ]
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=READER)

    surname = models.CharField(max_length=30, unique=False, blank=True, null=True)
    lastname = models.CharField(max_length=30, unique=False, blank=True, null=True)

    # номер читательского билета
    library_card_number = models.CharField(max_length=20, unique=True, blank=True, null=True)

    register_date = models.DateField(blank=True, null=True)

    # читательский зал
    reader_room = models.ForeignKey('ReadingRoom', on_delete=models.CASCADE, blank=True, null=True)

    # номер паспорта
    passport_code = models.CharField(max_length=11, default='5700 620000', blank=True)

    birth_date = models.DateField(default='1989-01-10', blank=True)
    home_address = models.CharField(max_length=150, default='some address', blank=True)
    phone = models.CharField(max_length=11, unique=True)

    SECONDARY = 1
    HIGH = 2

    education_choises = [
        (SECONDARY, 'Среднее'),
        (HIGH, 'Высшее'),
    ]
    education = models.PositiveSmallIntegerField(choices=education_choises, blank=True, null=True)
    # признак наличия ученой степени
    is_have_degree = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f'{self.username}'


class Publisher(models.Model):
    name = models.CharField(max_length=150)


class Book(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField(default=2015, blank=True)
    authors = models.ManyToManyField(User, related_name='authors', blank=True, null=True)

    # шифр
    cypher = models.CharField(max_length=20, unique=True)

    # издатель (издательство)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, blank=True, null=True, related_name='publisher')

    def __str__(self):
        return self.title


class Library(models.Model):
    name = models.CharField(max_length=200, unique=True)
    address = models.CharField(max_length=200, blank=True, default='Random street, 15')

    def __str__(self):
        return f'{self.name} (pk={self.pk})'


class ReadingRoom(models.Model):
    number = models.PositiveSmallIntegerField(unique=True)
    # вместимость читального зала
    capacity = models.PositiveSmallIntegerField(default=20, blank=True)
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='library')

    def __str__(self):
        return f'Читальный зал №{self.number} библиотеки "{self.library.name}"' # (pk={self.pk})'

"""
модель, описывающая экземпляр книги
основная задача данной модели заключается в хранении истории, 
т.к. модель ссылается на читателя и имеет дату закрепления книги за читателем
"""
class BookCopy(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book')
    reader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reader', null=True, blank=True)
    reading_room = models.ManyToManyField(ReadingRoom)
    own_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'Экземпляр книги "{self.book.title}"'

    """
    количество экземпляров книги в каждом зале не нужно хранить в БД,
    т.к. его можно будет посчитать запросом
    """
```

- views.py
``` py
import json
from collections import defaultdict
from datetime import datetime

from django.forms.models import model_to_dict
from dateutil.relativedelta import relativedelta
from django.db.models import F, Count, Sum, Q
from django.db.models.functions import Extract, Now
from rest_framework import generics, serializers, permissions, mixins
from rest_framework.generics import get_object_or_404, RetrieveUpdateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.permissions import IsLibraryWorker
from api.serializers import *
from library_app.models import *


class CreateUserView:
    model = User


class CreateReaderView(CreateUserView, generics.CreateAPIView):
    serializer_class = ReaderSerializer
    permission_classes = [AllowAny]


class CreateAuthorView(CreateUserView, generics.CreateAPIView):
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]


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
            return Response({'detail': "Недостаточно прав (авторизируйтесь как работник библиотеки)"''})

        queryset = User.objects.filter(register_date__lt=(datetime.now().date() - relativedelta(months=12)))
        response = {'detail': [user.username for user in queryset]}
        queryset.delete()
        return Response(response)


class DeleteBookCopyView(APIView):
    def post(self, request, **kwargs):
        if request.user.role != User.LIBRARY_WORKER:
            return Response({'detail': "Недостаточно прав (авторизируйтесь как работник библиотеки)"''})

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


class EditUserView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_url_kwarg = 'username'
    lookup_field = 'username'


class BooksCopiesView(generics.ListAPIView):
    queryset = BookCopy.objects.all()
    serializer_class = BookCopySerializer


class GetBookView(APIView):
    def post(self, request, **kwargs):
        username = kwargs['username']
        user = get_object_or_404(User, username=username)
        data = request.data
        book_title = data['book']

        if BookCopy.objects.filter(reader__username=username, book__title=book_title).exists():
            return Response({'detail': f'Пользователь {username} уже взял книгу {book_title}'})

        book_copy = BookCopy.objects.filter(Q(book__title=book_title) & Q(reader__isnull=True))

        if not book_copy:
            return Response({'detail': f'Нет свободных экземпляров книги {book_title} или такой книги не существует'})

        book_copy = book_copy.first()
        book_copy.reader = user
        book_copy.save()
        return Response({'detail': f'Пользователь {username} взял книгу {book_title}'})


class ReturnBookView(APIView):
    def post(self, request, **kwargs):
        username = kwargs['username']
        user = get_object_or_404(User, username=username)
        data = request.data
        book_title = data['book']

        if not BookCopy.objects.filter(reader__username=username, book__title=book_title).exists():
            return Response(
                {'detail': f'Пользователь {username} не может вернуть книгу {book_title}, т.к. ранее не брал ее'})

        book_copy = BookCopy.objects.get(Q(book__title=book_title) & Q(reader=user))

        if not book_copy:
            return Response(
                {'detail': f'Книги {book_title} не существует, либо эта книга не взята пользователем {username}'})

        book_copy.reader = None
        book_copy.save()
        return Response({'detail': f'Пользователь {username} вернул книгу {book_title}'})


class GetUserInfoView(APIView):
    def get(self, request, **kwargs):
        user = get_object_or_404(User, username=kwargs['username'])
        user_obj = model_to_dict(user)
        restricted = ['id', 'password', 'date_joined', '_state',
                      'surname', 'lastname', 'role',
                      'is_staff', 'is_active', 'last_login',
                      'is_superuser', 'groups', 'user_permissions',
                      'reader_room', 'education', 'first_name', 'last_name']
        return Response({'detail': user_obj})
    # [f'{key}: {user.__dict__[key]}' for key in user.__dict__ if key not in restricted]
```

- serializers.py
``` py
from datetime import datetime

from rest_framework import serializers, generics
from rest_framework.response import Response

from library_app.models import *


# Специальный сериализатор для регистрации читателя работником библиотеки
class LibraryWorkerReaderUpdateSerializer(serializers.ModelSerializer):

    def update(self, instance, data):
        # меняем в БД дату регистрации в библиотеке, если номер читательского билета непуст
        instance.register_date = datetime.now().date() if data['library_card_number'] else None
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ['library_card_number', 'reader_room', 'register_date']


class ReaderSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, data):
        # пишем в БД дату регистрации в библиотеке, если номер читательского билета непуст
        data['register_date'] = datetime.now().date() if data['library_card_number'] else None
        data['role'] = User.READER
        user = User.objects.create_user(**data)
        return user

    class Meta:
        model = User
        fields = ('username', 'password', 'phone', 'library_card_number', 'reader_room', 'register_date', 'education', 'is_have_degree')


class AuthorSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, data):
        data['role'] = User.AUTHOR
        user = User.objects.create_user(**data)
        return user

    class Meta:
        model = User
        fields = ('username', 'password')


class ReadingRoomSerizalier(serializers.ModelSerializer):
    class Meta:
        model = ReadingRoom
        fields = '__all__'


class BookCopySerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(read_only=True, slug_field='title')
    reader = serializers.SlugRelatedField(read_only=True, slug_field='username')

    # StringRelatedField позволяет получить значение из метода модели __str__
    # в данном случае из модели ReadingRoom
    reading_rooms = serializers.StringRelatedField(many=True, source='reading_room')

    class Meta:
        model = BookCopy
        exclude = ['id', 'reading_room']


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['title', 'year', 'cypher']

    # Можно переопределить метод create способом ниже, если еще понадобиться создать экземпляр книги
    # def create(self, data):
    #     book = Book.objects.create(**data)
    #     book_copy = BookCopy.objects.create(book=book)
    #     request_data = self.context['request'].data
    #     book_copy.reading_room.set(request_data['reading_room'])
    #     return book


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['id', 'password', 'date_joined',
                   'surname', 'lastname', 'role',
                   'is_staff', 'is_active', 'last_login',
                   'is_superuser', 'groups', 'user_permissions',
                   'reader_room', 'education', 'first_name', 'last_name']
```

- urls.py
``` py
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
