# Лабораторная работа №3
Описание работы

Задание 2. Библиотека

Создать программную систему, предназначенную для работников библиотеки. Такая система должна обеспечивать хранение сведений об имеющихся в библиотеке книгах, о читателях библиотеки и читальных залах.

Для каждой книги в БД должны храниться следующие сведения: название книги, автор (ы), издательство, год издания, раздел, число экземпляров этой книги в каждом зале библиотеки, а также шифр книги и дата закрепления книги за читателем. Книги могут перерегистрироваться в другом зале.

Сведения о читателях библиотеки должны включать номер читательского билета, ФИО читателя, номер паспорта, дату рождения, адрес, номер телефона, образование, наличие ученой степени.

Читатели закрепляются за определенным залом, могут переписаться в другой зал и могут записываться и выписываться из библиотеки.

Библиотека имеет несколько читальных залов, которые характеризуются номером, названием и вместимостью, то есть количеством людей, которые могут одновременно работать в зале.

Библиотека может получать новые книги и списывать старые. Шифр книги может измениться в результате переклассификации, а номер читательского билета в результате перерегистрации.


## Основные файлы с кодом

* `models.py` - сущности базы

```python
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE


class User(AbstractUser):
    tel = models.CharField(verbose_name='Телефон', max_length=15, null=True, blank=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'tel']

    def __str__(self):
        return self.username


class Instance(models.Model):
    id_instance = models.AutoField("ID_экземпляра", primary_key=True)
    section = models.CharField(max_length=20, verbose_name='Раздел')
    code = models.CharField(max_length=20, verbose_name='Артикул')
    year = models.IntegerField(verbose_name='Год издания')
    conditions = (
        ('х', 'хорошее'),
        ('у', 'удовлетворительное'),
        ('с', 'старое'),
    )
    condition = models.CharField(max_length=1, choices=conditions, verbose_name='Состояние экземпляра')
    book = models.ForeignKey('Book', verbose_name='Книга', on_delete=CASCADE)

    def __str__(self):
        return self.code


class Book(models.Model):
    id_book = models.AutoField("ID_книги", primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Название')
    author = models.CharField(max_length=70, verbose_name="ФИО автора")
    publisher = models.CharField(max_length=30, verbose_name='Издательство')

    def __str__(self):
        return self.name


class Reader(models.Model):
    ticket = models.CharField(max_length=20, verbose_name='Номер читательского билета')
    name = models.CharField(max_length=70, verbose_name="ФИО")
    passport = models.CharField(max_length=20, verbose_name='Номер паспорта')
    birth_date = models.DateField(verbose_name='Дата рождения')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    educations = (
        ('н', 'начальное'),
        ('с', 'среднее'),
        ('в', 'высшее'),
    )
    education = models.CharField(max_length=1, choices=educations, verbose_name='Образование')
    degree = models.BooleanField(default=False, verbose_name='Наличие ученой степени')
    registration_date = models.DateField(verbose_name='Дата регистрации')
    instances = models.ManyToManyField('Instance', verbose_name='Взятые книги', through='ReaderBook',
                                       related_name='reader_book')
    room = models.ForeignKey('Room', verbose_name='Зал, за которым закреплен читатель', on_delete=CASCADE, null=True)

    def __str__(self):
        return self.name


class ReaderRoom(models.Model):
    reader = models.ForeignKey('Reader', verbose_name='Читатель', on_delete=CASCADE)
    room = models.ForeignKey('Room', verbose_name='Зал', on_delete=CASCADE)
    date = models.DateField(verbose_name='Дата закрепления зала', null=True)


class BookInst(models.Model):
    inst = models.ForeignKey('Instance', verbose_name='Экземпляр', on_delete=CASCADE)
    book = models.ForeignKey('Book', verbose_name='Книга', on_delete=CASCADE)


class ReaderBook(models.Model):
    reader = models.ForeignKey('Reader', verbose_name='Читатель', on_delete=CASCADE)
    book = models.ForeignKey('Instance', verbose_name='Экземпляр', on_delete=CASCADE)
    date = models.DateField(verbose_name='Дата выдачи экземпляра книги', null=True)


class BookRoom(models.Model):
    book = models.ForeignKey('Instance', verbose_name='Книга', on_delete=CASCADE)
    room = models.ForeignKey('Room', verbose_name='Зал', on_delete=CASCADE)


class Room(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    capacity = models.IntegerField(verbose_name='Вместимость')
    books = models.ManyToManyField('Instance', verbose_name='Книги', through='BookRoom', related_name='book_room')

    def __str__(self):
        return self.name
```

* `views.py` - функционал

```python
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.utils import timezone
from .models import *
from .serializers import *
from datetime import datetime, timedelta
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework import generics
from rest_framework.views import APIView, Response
from datetime import date


# просмотр информации о читателях
class ReaderListAPIView(ListAPIView):
    serializer_class = ReaderSerializer
    queryset = Reader.objects.all()


# создание читателя
class CreateReader(CreateAPIView):
    serializer_class = ReaderSerializer
    queryset = Reader.objects.all()


# просмотр всех произведений в библиотеке
class BookListAPIView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


# появление нового произведения в библиотеке
class CreateBook(CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


# просмотр экземпляров произведений
class InstanceListAPIView(ListAPIView):
    serializer_class = InstanceSerializer
    queryset = Instance.objects.all()


class CreateInstance(CreateAPIView):
    serializer_class = InstanceSerializer
    queryset = Instance.objects.all()


# редактирование и удаление произведений
class OneBook(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


# редактирование и удаление экземпляров
class OneInstance(RetrieveUpdateDestroyAPIView):
    serializer_class = InstanceSerializer
    queryset = Instance.objects.all()


# редактирование и удаление читателей
class OneReader(RetrieveUpdateDestroyAPIView):
    serializer_class = ReaderSerializer
    queryset = Instance.objects.all()


# бронь книги
class BookReaders(CreateAPIView):
    serializer_class = ReaderBookSerializer
    queryset = ReaderBook.objects.all()


# просмотр комнат
class RoomListAPIView(ListAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


# создание комнат
class RoomCreateAPIView(CreateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


# редактирование и удаление комнат
class OneRoom(RetrieveUpdateDestroyAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


# закрепление книги за комнатой
class RoomBook(CreateAPIView):
    serializer_class = BookRoomSerializer
    queryset = BookRoom.objects.all()


# закрепление читателя за комнатой
class RoomReader(CreateAPIView):
    serializer_class = ReaderRoomSerializer
    queryset = ReaderRoom.objects.all()


class BookInst(CreateAPIView):
    serializer_class = BookInstSerializer
    queryset = BookInst.objects.all()


class ReadersInst(generics.RetrieveAPIView):
    serializer_class = ReaderInstsSerializer
    queryset = Reader.objects.all()

class RecentlyBookDate(ListAPIView):
    # serializer_class = RecentlyBookDateSerializer
    # queryset = ReaderBook.objects.all()


    def get(self, request):
        today = date.today()
        reader = ReaderBook.objects.filter(date__lte=today)
        content = {"reader": reader}
        return Response(content)

```

* `serializers.py` - преобразование данных БД в нативные типы данных Python

```python
from django.utils import timezone
from rest_framework import serializers
from .models import *


class ReaderSerializer(serializers.ModelSerializer):
    books = serializers.SlugRelatedField(read_only=True, many=True, slug_field='books')

    class Meta:
        model = Reader
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class InstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instance
        fields = "__all__"


class ReaderBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReaderBook
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    books = serializers.SlugRelatedField(read_only=True, many=True, slug_field='name')

    class Meta:
        model = Room
        fields = "__all__"


class BookRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookRoom
        fields = "__all__"


class ReaderRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReaderRoom
        fields = "__all__"


class BookInstSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInst
        fields = "__all__"


class ReaderInstsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = ["instances"]


class RecentlyBookDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReaderBook
        fields = ["reader"]

```


* `urls.py` - юрлы адресов нашего сайта

```python
from django.urls import path
from .views import *

urlpatterns = [
    path('readers/list/', ReaderListAPIView.as_view()),
    path('readers/create/', CreateReader.as_view()),
    path('readers/<int:pk>/', OneReader.as_view()),
    path('books/list/', BookListAPIView.as_view()),
    path('books/create/', CreateBook.as_view()),
    path('books/<int:pk>/', OneBook.as_view()),
    path('inst/list/', InstanceListAPIView.as_view()),
    path('inst/create/', CreateInstance.as_view()),
    path('inst/<int:pk>/', OneInstance.as_view()),
    path('rooms/list/', RoomListAPIView.as_view()),
    path('rooms/create/', RoomCreateAPIView.as_view()),
    path('rooms/<int:pk>/', OneRoom.as_view()),
    path('book/readers/', BookReaders.as_view()),
    path('book/room/', RoomBook.as_view()),
    path('room/readers/', RoomReader.as_view()),
    path('book/inst/', BookInst.as_view()),
    path('readers/inst/<int:pk>', ReadersInst.as_view()),
]
```


Эндпоинт - по привязки книги к пользователю

```python
**URL** : `/library/book/readers`

**Method** : `POST`

**Auth required** : YES

**Permissions required** : None

**Body** : {
    reader: 2 
    book: 2
    date: '2022-01-01'
}

**Headers** : {
    'Content-Type': 'application/json'
}

**Data constraints** : `{
    
}`

**Code** : `200 OK`

**Content** : `{[]}`

'''json

'''
```