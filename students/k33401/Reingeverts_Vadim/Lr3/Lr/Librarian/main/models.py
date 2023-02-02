import datetime
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class User(AbstractUser):
    last_name = models.CharField(max_length=100, blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    middle_name = models.CharField(max_length=100, blank=True)

    library = models.ForeignKey(
        'Library', on_delete=models.CASCADE, blank=True, null=True)
    reading_room = models.ForeignKey(
        'ReadingRoom', on_delete=models.CASCADE, blank=True, null=True)
    serial_number = models.CharField(max_length=20)
    passport = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=250, blank=True)
    education_level = models.CharField(max_length=250, blank=True)
    phone_number = PhoneNumberField(region="RU", blank=True)

    ACADEMIC_DEGREES = (
        ('', None),
        ('Associate Degree', 'Associate Degree'),
        ('Bachelor\'s Degree', 'Bachelor\'s Degree'),
        ('Master\'s Degree', 'Master\'s Degree'),
        ('Doctoral Degree', 'Doctoral Degree'),
    )
    academic_degree = models.CharField(
        max_length=20, choices=ACADEMIC_DEGREES, default=None, blank=True, null=True)

    def __str__(self):
        if (self.first_name or self.last_name):
            return self.first_name + " " + self.last_name
        else:
            return self.username


class Library(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Libraries"


class ReadingRoom(models.Model):
    name = models.CharField(max_length=100)

    library = models.ForeignKey('Library', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=250)
    authors = models.CharField(max_length=250, blank=True)
    publisher = models.CharField(max_length=250, blank=True)
    pub_date = models.DateField(blank=True, null=True)
    series = models.CharField(max_length=250, blank=True)  # "раздел"
    total_amount = models.IntegerField(
        default=100, validators=[MinValueValidator(0)])
    isbn = models.CharField(max_length=17, blank=True)  # "шифр"

    reading_rooms = models.ManyToManyField(
        'ReadingRoom', through="ReadingRoomBook")

    borrowers = models.ManyToManyField('User', through="BookUser", blank=True)

    def set_authors(self, authors):
        self.authors = ", ".join(authors)

    def get_authors(self):
        return self.authors.split(', ')

    def get_avaliable_amount(self):
        borrowed = self.borrowers.filter(bookuser__returned_date__isnull=False)
        return self.total_amount - borrowed.count()

    def __str__(self):
        return self.title + " (" + str(self.total_amount) + " total)"


class BookUser(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    borrow_date = models.DateField(default=datetime.date.today)
    returned_date = models.DateField(blank=True, null=True)

    def is_returned(self):
        return self.returned_date is not None

    def __str__(self):
        return self.user.__str__() + " | " + self.book.__str__()

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(
                returned_date__gt=models.F('borrow_date')), name='date_check', violation_error_message='Borrow date must be earlier than returned date.'),
        ]


class ReadingRoomBook(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    reading_room = models.ForeignKey('ReadingRoom', on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

    def __str__(self):
        return self.book + " | " + self.reading_room
