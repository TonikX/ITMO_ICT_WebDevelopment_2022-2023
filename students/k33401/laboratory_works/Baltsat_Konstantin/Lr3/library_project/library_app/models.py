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


class ReaderBook(models.Model):
    #book = models.ForeignKey('Book', on_delete=models.CASCADE, verbose_name='Книга')
    id_rb = models.IntegerField(verbose_name='номер выдачи', blank=True, null=False, primary_key=True)
    id_copy = models.ForeignKey("Copy", verbose_name='Id_ex', on_delete=models.CASCADE)
    #book = models.ForeignKey('Copy', verbose_name='Книга', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', verbose_name='Книга', on_delete=models.CASCADE)
    reader = models.ForeignKey('Reader', on_delete=models.CASCADE, verbose_name='Читатель')
    issue_date = models.DateField(verbose_name='Дата выдачи', blank=True, null=True)
    due_date = models.DateField(verbose_name='Дата возврата', blank=True, null=True)