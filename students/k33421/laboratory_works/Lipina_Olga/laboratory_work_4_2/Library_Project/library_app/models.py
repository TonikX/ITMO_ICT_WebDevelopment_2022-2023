from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE



# class User(AbstractUser):
#     """Пользователь системы"""
#     mobile = models.CharField(verbose_name='Мобильный телефон',
#                               max_length=25,
#                               null=True,
#                               blank=True)
#
#     REQUIRED_FIELDS = ['first_name', 'last_name', 'mobile']
#
#     def __str__(self):
#         return self.username

class Book(models.Model):
    """Книга"""
    id = models.AutoField("ID книги в базе", primary_key=True)
    book_name = models.CharField(max_length=50, verbose_name='Название')
    author = models.CharField(max_length=70, verbose_name = "Автор")
    section = models.CharField(max_length=20, verbose_name='Раздел', null=True, blank=True)


    def __str__(self):
        return self.book_name

class InstanceBook(models.Model):
    """Экземпляр книги"""
    id = models.AutoField("ID экземпляра книги", primary_key=True)
    cypher = models.CharField(max_length=20, verbose_name='Шифр')
    year_published = models.IntegerField(verbose_name='Год издания')
    publisher  =models.CharField(max_length=20, verbose_name='Издатель')
    conditions = (
        ('g', 'good'),
        ('n', 'normal'),
        ('b', 'bad'),
    )
    condition = models.CharField(max_length=1, choices=conditions, verbose_name='Состояние экземпляра')
    book = models.ForeignKey('Book', verbose_name='Книга', on_delete=CASCADE)
    instance_hall = models.ForeignKey('Hall', on_delete=models.CASCADE, verbose_name='Зал',
                                    blank=True, null=True)
    who_reads = models.ManyToManyField('Reader', through='BooksOnHands', verbose_name='Читатель')

    def __str__(self):
        return f"{self.book} {self.id}"

class InstancePlace(models.Model):
    """Экземпляр-Холл связь"""
    book = models.ForeignKey('InstanceBook', verbose_name='Экземпляр книги', on_delete=CASCADE)
    room = models.ForeignKey('Hall', verbose_name='Зал библиотеки', on_delete=CASCADE)
    def __str__(self):
        return f"{self.book}, {self.room}"

class Hall(models.Model):
    """Читальный зал"""
    name = models.CharField(max_length=50, verbose_name='Имя зала')
    capacity = models.IntegerField(verbose_name='Вместимость')
    books = models.ManyToManyField('InstanceBook',
                                   verbose_name='Книги',
                                   through='InstancePlace',
                                   related_name='instance_place')
    readers = models.ManyToManyField('Reader',
                                   verbose_name='Читатели',
                                   through='ReaderHall',
                                   related_name='reader_place')

    def __str__(self):
        return self.name

class BooksOnHands(models.Model):
    """Читатель-экземляр. Книги на руках"""
    reader = models.ForeignKey('Reader', verbose_name='Читатель', on_delete=CASCADE)
    instance = models.ForeignKey('InstanceBook', verbose_name='Экземпляр книги', on_delete=CASCADE)
    date_register = models.DateField(default=datetime.now().date, verbose_name='Дата выдачи', null=True, blank=True)
    def __str__(self):
        return f"{self.reader.name}, {self.instance.book.book_name}"

class ReaderHall(models.Model):
    reader = models.ForeignKey('Reader', verbose_name='Читатель', on_delete=CASCADE)
    hall = models.ForeignKey('Hall', verbose_name='Зал', on_delete=CASCADE)
    date = models.DateField(verbose_name='Дата закрепления зала', blank=True, null=True)
    def __str__(self):
        return f"{self.reader.name.split()[0]}, {self.hall}"


class Reader(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)

    REQUIRED_FIELDS = ['library_pass', 'name', 'birth_date',
                      'address', 'education_level', 'phone_number', 'degree']#, 'education_level']
              #         'degree']
    library_pass = models.CharField(max_length=20, verbose_name='Читательский билет')
    name = models.CharField(max_length=70, verbose_name="ФИО")
    birth_date = models.DateField(verbose_name='День рождения',  blank=True, null=True)
    address = models.CharField(max_length=100, verbose_name='Адрес',  blank=True, null=True)
    phone_number = models.CharField(max_length=20, verbose_name='Телефон',  blank=True, null=True)
    education_variations = (
        ('e', 'elementary'),
        ('s', 'secondary'),
        ('c', 'college'),
    )
    education_level = models.CharField(max_length=1, choices=education_variations, default='e', verbose_name='Образование')
    degree = models.BooleanField(default=False, verbose_name='Есть ли уч степент')
    # registration_date = models.DateField(verbose_name='Дата регистрации')
    instances_on_hands = models.ManyToManyField('InstanceBook',
                                                verbose_name='Книги на руках',
                                                through='BooksOnHands',
                                                related_name='instance_reader')
    reader_hall = models.ForeignKey('Hall', on_delete=models.CASCADE, verbose_name='Зал',
                                    blank=True, null=True)
    def __str__(self):
        if self.is_superuser:
            return f'superuser {self.username}'
        return f'reader {self.username}'