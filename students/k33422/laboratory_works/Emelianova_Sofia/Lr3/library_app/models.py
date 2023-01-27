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