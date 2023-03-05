from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class BookCategory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Book(models.Model):
    book_category = models.ForeignKey(BookCategory, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    isbn = models.BigIntegerField()
    page_count = models.IntegerField()
    price = models.IntegerField()
    has_illustrations = models.BooleanField(null=True, blank=True)
    def __str__(self):
        return self.title

class Author(models.Model):
    books = models.ManyToManyField(Book, through='Authorship', related_name='author')
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.last_name + ' ' + self.first_name

class Authorship(models.Model):
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    order_number = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return str(self.author) + ' ' + str(self.book) + ' ' + str(self.order_number)

class Edition(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    date_created = models.DateTimeField()
    volume = models.IntegerField()
    def __str__(self):
        return str(self.book) + ' ' + str(self.id)

class OrderManager(AbstractUser):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    position = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100, null=True, blank=True)
    REQUIRED_FIELDS = ['last_name', 'first_name', 'phone', 'position', 'patronymic', 'email']

class Customer(models.Model):
    orders = models.ManyToManyField(OrderManager, through='BooksOrder', related_name='customer')
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    address = models.CharField(max_length=300)
    patronymic = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return str(self.last_name) + ' ' + str(self.first_name)

class BooksOrder(models.Model):
    books = models.ManyToManyField(Book, through='OrderBook', related_name='books_order')
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    order_manager = models.ForeignKey(OrderManager, on_delete=models.PROTECT)
    date_created = models.DateTimeField()
    date_until = models.DateTimeField()
    status = models.CharField(max_length=20)

class OrderBook(models.Model):
    books_order = models.ForeignKey(BooksOrder, on_delete=models.PROTECT)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    volume = models.IntegerField()























