from typing import AbstractSet
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE

class User(AbstractUser):
    tel = models.CharField(verbose_name='Телефон', max_length=15, null=True, blank=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'tel']

    def __str__(self):
        return self.username


class BookRoom(models.Model):
    book = models.ForeignKey('Book', verbose_name='Книга', on_delete=CASCADE)
    room = models.ForeignKey('Room', verbose_name='Зал', on_delete=CASCADE)

class Book(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    author = models.ForeignKey('Author', on_delete=CASCADE, verbose_name='Автор', blank=True, null=True)
    publisher = models.ForeignKey('Publisher', on_delete=CASCADE, verbose_name='Издательство', blank=True, null=True)
    year = models.IntegerField(verbose_name='Год издания')
    section = models.ForeignKey('Section', on_delete=CASCADE, verbose_name='Раздел', blank=True, null=True)
    code = models.CharField(max_length=20, verbose_name='Шифр')
    date = models.DateTimeField(verbose_name='Дата закрепления за читателем')

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=70, verbose_name = "ФИО")
    
    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=30, verbose_name='Издательство')

    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=20, verbose_name='Раздел')

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
    books = models.ManyToManyField('Book', verbose_name='Взятые книги', through='ReaderBook', related_name='reader_book')
    room = models.ForeignKey('Room', verbose_name='Зал, за которым закреплен читатель', on_delete=CASCADE, null=True)

    def __str__(self):
        return self.name

class ReaderRoom(models.Model):
    reader = models.ForeignKey('Reader', verbose_name='Читатель', on_delete=CASCADE)
    room = models.ForeignKey('Room', verbose_name='Зал', on_delete=CASCADE)

class ReaderBook(models.Model):
    reader = models.ForeignKey('Reader', verbose_name='Читатель', on_delete=CASCADE)
    book = models.ForeignKey('Book', verbose_name='Книга', on_delete=CASCADE)
    date = models.DateField(verbose_name='Дата выдачи книги', null=True)

class Library(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    room = models.ManyToManyField('Room', verbose_name='Зал', through='LibraryRoom', related_name='library_room')

    def __str__(self):
        return self.name

class LibraryRoom(models.Model):
    library = models.ForeignKey('Library', verbose_name='Библиотека', on_delete=CASCADE)
    room = models.ForeignKey('Room', verbose_name='Зал', on_delete=CASCADE)

class Room(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    capacity = models.IntegerField(verbose_name='Вместимость')
    books = models.ManyToManyField('Book', verbose_name='Книги', through='BookRoom', related_name='book_room')

    def __str__(self):
        return self.name

