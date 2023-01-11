# ЛАБОРАТОРНАЯ РАБОТА №3

## ОПИСАНИЕ ЗАДАНИЯ
# ВАРИАНТ 2

Задание 2. Библиотека
Создать программную систему, предназначенную для работников библиотеки. Такая система должна обеспечивать хранение сведений об имеющихся в библиотеке книгах, о читателях библиотеки и читальных залах.

Для каждой книги в БД должны храниться следующие сведения: название книги, автор (ы), издательство, год издания, раздел, число экземпляров этой книги в каждом зале библиотеки, а также шифр книги и дата закрепления книги за читателем. Книги могут перерегистрироваться в другом зале.

Сведения о читателях библиотеки должны включать номер читательского билета, ФИО читателя, номер паспорта, дату рождения, адрес, номер телефона, образование, наличие ученой степени.

Читатели закрепляются за определенным залом, могут переписаться в другой зал и могут записываться и выписываться из библиотеки.

Библиотека имеет несколько читальных залов, которые характеризуются номером, названием и вместимостью, то есть количеством людей, которые могут одновременно работать в зале.

Библиотека может получать новые книги и списывать старые. Шифр книги может измениться в результате переклассификации, а номер читательского билета в результате перерегистрации.

Основные файлы с кодом
* models.py
``` py
from django.db import models
from django.contrib.auth.models import AbstractUser


class Book(models.Model):
    title =      models.CharField(max_length=800, verbose_name='Название')
    authors =    models.CharField(max_length=5000, verbose_name='Автор(ы)')
    publisher =   models.CharField(max_length=79, verbose_name='Издательство')
    publication_year  = models.IntegerField(verbose_name='Год издания')
    genre =        models.CharField(max_length=100, verbose_name='Жанр')
    book_cypher =  models.CharField(max_length=50, verbose_name='Шифр')
    book_hall =    models.ManyToManyField('Hall','BokkCopy', through='BookInHall', verbose_name='Зал')
    book_reader  = models.ManyToManyField('Reader', through='ReaderBook', verbose_name='Читатель')
    
    def __str__(self):
        return self.title
    

class Hall(models.Model):
    number = models.IntegerField(verbose_name='Номер')
    title = models.CharField(max_length=500, verbose_name='Название')
    capacity = models.IntegerField(verbose_name='Вместимость')
    
    def __str__(self):
        return str(self.number) + " - " + self.title


class BookInHall(models.Model):
    book = models.ForeignKey('Book',  on_delete=models.CASCADE, verbose_name='Книга')
    hall = models.ForeignKey('Hall', on_delete=models.CASCADE, verbose_name='Зал',)
    count = models.IntegerField(verbose_name='Число экземпляров')

    def __str__(self):
        return str(self.book) + " в зале " + str(self.hall) + ": " + str(self.count)


class Reader(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=200)

    REQUIRED_FIELDS = ['card_number', 'first_name', 'last_name',
                       'passport', 'date_of_birth', 'address', 'phone',
                       'education', 'degree']

    card_number = models.IntegerField(verbose_name='Читательский билет', blank=True, null=True)
    first_name = models.CharField(max_length=25, verbose_name='Имя', blank=True, null=True)
    last_name = models.CharField(max_length=30, verbose_name='Фамилия', blank=True, null=True)
    passport = models.CharField(max_length=15, verbose_name='Паспорт', blank=True, null=True)
    date_of_birth = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    address = models.CharField(max_length=300, verbose_name='Адрес', blank=True, null=True)
    phone = models.CharField(max_length=11, verbose_name='Телефон', blank=True, null=True)

    education_options = (
        ('Среднее общее', 'Среднее общее'),
        ('Среднее специальное', 'Среднее специальное'),
        ('Высшее', 'Высшее'),
        ('Неоконченное высшее', 'Неоконченное высшее'),
        ('Неоконченное среднее', 'Неоконченное среднее'),
    )
    education = models.CharField(max_length=4000, choices=education_options, default='-',
                                 verbose_name='Образование', blank=True, null=True)
    degree = models.BooleanField(default=False, verbose_name='Ученая степень', blank=True, null=True)
    reader_hall = models.ForeignKey('Hall', on_delete=models.CASCADE, verbose_name='Зал',
                                    blank=True, null=True)
    reader_book = models.ManyToManyField('Book', through='ReaderBook', verbose_name='Книга')

'''    def __str__(self):
        if self.is_superuser:
            return 'superuser'
        return self.last_name + ' ' + self.first_name'''

class Copy(models.Model):
    id_copy = models.AutoField("ID_экземпляра", primary_key=True)
    section = models.CharField(max_length=20, verbose_name='Раздел')
    code = models.CharField(max_length=20, verbose_name='Артикул')
    year = models.IntegerField(verbose_name='Год издания')
    conditions = ( 
        ('х', 'хорошее'),
        ('у', 'удовлетворительное'),
        ('с', 'старое'),
    )
    condition = models.CharField(max_length=1, choices=conditions, verbose_name='Состояние экземпляра')
    book = models.ForeignKey('Book', verbose_name='Книга', on_delete=models.CASCADE)


    def __str__(self):
        return self.code

class ReaderBook(models.Model):
    #book = models.ForeignKey('Book', on_delete=models.CASCADE, verbose_name='Книга')
    id_rb = models.IntegerField(verbose_name='номер выдачи', blank=True, null=False, primary_key=True)
    id_copy = models.ForeignKey("Copy", verbose_name='Id_ex', on_delete=models.CASCADE)
    #book = models.ForeignKey('Copy', verbose_name='Книга', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', verbose_name='Книга', on_delete=models.CASCADE)
    reader = models.ForeignKey('Reader', on_delete=models.CASCADE, verbose_name='Читатель')
    issue_date = models.DateField(verbose_name='Дата выдачи', blank=True, null=True)
    due_date = models.DateField(verbose_name='Дата возврата', blank=True, null=True)
``` 

* serializers.py
``` py
from rest_framework import serializers
from .models import *



class CopySerializer(serializers.ModelSerializer):
   class Meta:
     model = Copy
     fields = "__all__"
     



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

     
class BookInhallSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInHall
        fields = "__all__"
     
class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = "__all__"


class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = "__all__"
        #exclude=('password', )

    def create(self, validated_data):
        user = Reader(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user  


class BookRetrieveSerializer(serializers.ModelSerializer):
    book_hall = HallSerializer(many=True)
    book_reader = ReaderSerializer(many=True)

    class Meta:
        model = Book
        fields = "__all__"


class ReaderRetrieveSerializer(serializers.ModelSerializer):
    reader_hall = HallSerializer()
    reader_book = BookSerializer(many=True)

    class Meta:
        model = Reader
        fields = "__all__"    
        
        
        
class ReaderBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReaderBook
        fields = "__all__"

    '''def create(self, validated_data):
        user = ReaderBook(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user'''
    
class ReaderBookRetrieveSerializer(serializers.ModelSerializer):
    reader_hall = HallSerializer()
    reader_book = BookSerializer(many=True)

    class Meta:
        model = ReaderBook
        fields = "__all__"
```
* views.py
``` py
from django.db.models import Sum

from .serializers import *
from rest_framework.generics import *


class CopyListAPIView(ListAPIView):
    serializer_class = CopySerializer
    queryset = Copy.objects.all()

class CopyCreateAPIView(CreateAPIView):
    serializer_class = CopySerializer
    queryset = Copy.objects.all()


class CopykRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CopySerializer
    queryset = Copy.objects.all()

class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    
#class CopyRetrieveAPIView(RetrieveAPIView):
    #serializer_class = CopyRetrieveSerializer
    #queryset = Copy.objects.all()

class BookListAPIView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()



class BookCreateAPIView(CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookRetrieveAPIView(RetrieveAPIView):
    serializer_class = BookRetrieveSerializer
    queryset = Book.objects.all()


class ReaderListAPIView(ListAPIView):
    serializer_class = ReaderSerializer
    queryset = Reader.objects.all()


class ReaderCreateAPIView(CreateAPIView):
    serializer_class = ReaderSerializer
    queryset = Reader.objects.all()


class ReaderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ReaderSerializer
    queryset = Reader.objects.all()


class ReaderRetrieveAPIView(RetrieveAPIView):
    serializer_class = ReaderRetrieveSerializer
    queryset = Reader.objects.all() 

class BookInhallrListAPIView(ListAPIView):
    serializer_class = BookInhallSerializer
    queryset = BookInHall.objects.all()

class BookInhallCreateAPIView(CreateAPIView):
    serializer_class = BookInhallSerializer
    queryset = BookInHall.objects.all()
    
class BookInhallRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookInhallSerializer
    queryset = BookInHall.objects.all()


class HallrListAPIView(ListAPIView):
    serializer_class = HallSerializer
    queryset = Hall.objects.all()
    
class HallCreateAPIView(CreateAPIView):
    serializer_class = HallSerializer
    queryset = Hall.objects.all()
    
class HallRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = HallSerializer
    queryset = Hall.objects.all()



class ReaderBookListAPIView(ListAPIView):
    serializer_class = ReaderBookSerializer
    queryset = ReaderBook.objects.all()


class ReaderBookCreateAPIView(CreateAPIView):
    serializer_class = ReaderBookSerializer
    queryset = ReaderBook.objects.all()


class ReaderBookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ReaderBookSerializer
    queryset = ReaderBook.objects.all()


class ReaderRetrieveAPIView(RetrieveAPIView):
    serializer_class = ReaderRetrieveSerializer
    queryset = Reader.objects.all()
```
* urls.py
``` py

urlpatterns = [
    path('books/', BookListAPIView.as_view()),  # list of books
    path('books/create/', BookCreateAPIView.as_view()),  # create book
    path('books/<int:pk>/', BookRetrieveAPIView.as_view()),  # book info by id
    path('books/edit/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view()),
    path('readers/', ReaderListAPIView.as_view()),  # list of readers
    path('readers/create/', ReaderCreateAPIView.as_view()),  # create reader
    path('readers/<int:pk>/', ReaderRetrieveAPIView.as_view()),  # reader info by id
    path('readers/edit/<int:pk>/', ReaderRetrieveUpdateDestroyAPIView.as_view()),
    path('copies/', CopyListAPIView.as_view()), 
    path('copies/create/', CopyCreateAPIView.as_view()),
    path('bookinhall/create/', BookInhallCreateAPIView.as_view()), 
    path('readers-book/', ReaderBookListAPIView.as_view()),  # list of readers-book
    path('readers-book/create/', ReaderBookCreateAPIView.as_view()),  # create readerbook
    path('readers-book/edit/<int:pk>/', ReaderBookRetrieveUpdateDestroyAPIView.as_view()),
]
```