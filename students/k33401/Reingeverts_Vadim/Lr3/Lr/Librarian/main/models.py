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
    # "номер читательского билета"
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

    @classmethod
    def generate_random_serial(self):
        return User.objects.make_random_password(
            length=12, allowed_chars='1234567890')

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
    capacity = models.IntegerField(
        default=20, validators=[MinValueValidator(0)])

    library = models.ForeignKey('Library', on_delete=models.CASCADE)

    def get_empty_slots(self):
        return self.capacity - self.user_set.count()

    def get_all_books(self):
        return self.book_set.all()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=250)
    authors = models.CharField(max_length=250, blank=True)
    publisher = models.CharField(max_length=250, blank=True)
    pub_date = models.DateField("Publication date", blank=True, null=True)
    # "раздел"
    series = models.CharField(max_length=250, blank=True)
    total_stock = models.IntegerField(
        default=100, validators=[MinValueValidator(0)])
    # "шифр"
    isbn = models.CharField("ISBN", max_length=17, blank=True)

    reading_rooms = models.ManyToManyField(
        'ReadingRoom', through="ReadingRoomBook")

    def get_undesignated_stock(self):
        """
        Returns the amount of books that are not
        designated to any reading room
        """
        designated = self.reading_rooms.all().aggregate(
            stock=models.Sum('readingroombook__stock'))
        print("self.total_stock", self.total_stock,
              "designated['stock']", designated['stock'], "=", self.total_stock - designated['stock'])
        return self.total_stock - designated['stock']

    def set_authors(self, authors):
        self.authors = ", ".join(authors)

    def get_authors(self):
        return self.authors.split(', ')

    def __str__(self):
        return self.title + " (" + str(self.total_stock) + " total)"


class ReadingRoomBookUser(models.Model):
    reading_room_book = models.ForeignKey(
        'ReadingRoomBook', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    borrow_date = models.DateField(default=datetime.date.today)
    returned_date = models.DateField(blank=True, null=True)

    def is_returned(self):
        return self.returned_date is not None

    def return_book(self):
        self.returned_date = datetime.date.today

    def __str__(self):
        return self.user.__str__() + " | " + self.reading_room_book.__str__()

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(
                returned_date__gte=models.F('borrow_date')), name='date_check', violation_error_message='Borrow date must be earlier than returned date.'),
        ]


class ReadingRoomBook(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    reading_room = models.ForeignKey('ReadingRoom', on_delete=models.CASCADE)

    borrowers = models.ManyToManyField(
        'User', through="ReadingRoomBookUser", blank=True)
    stock = models.IntegerField(default=1, validators=[MinValueValidator(0)])

    def get_avaliable_stock(self):
        """
        Returns amount of avaliable books to be borrowed
        in a particular reading room of particular library
        """
        borrowed = self.borrowers.filter(
            readingroombookuser__returned_date__isnull=True)
        return self.stock - borrowed.count()

    def __str__(self):
        return self.book.__str__() + " | " + self.reading_room.__str__()
