from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

r = ()  # пустой картеж


class Registration_user(AbstractUser):
    username = models.CharField("Ник", max_length=30, null=False)
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "password"]

    first_name = models.CharField("Имя", max_length=30, null=False)
    last_name = models.CharField("Фамилия", max_length=30, null=False)
    passport_number = models.CharField("Номер паспорта", primary_key=True, max_length=30)
    password = models.CharField("Пароль", max_length=300, null=False)

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data["email"],
            name=validated_data["name"],
            password=validated_data["password"],
        )

        return user

    def __str__(self):
        return self.passport_number


class Flight(models.Model):
    number_flight = models.CharField("Номер рейса", primary_key=True, max_length=30)
    date = models.DateField("Дата вылета", null=False, unique=True)

    def __str__(self) -> str:
        return self.number_flight


class Ticket(models.Model):
    LIST_OF_PLASEC_IN_PLANE = [r + (f"{i}", f"{i}") for i in range(1, 31)]
    place_in_plane = models.CharField(
        "Место", primary_key=True, max_length=2, choices=LIST_OF_PLASEC_IN_PLANE, default="-1"
    )
    passport_number = models.ForeignKey(Registration_user, on_delete=models.CASCADE)
    number_flight = models.ForeignKey(Flight, on_delete=models.CASCADE)


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    number_flight = models.ForeignKey(
        Flight, on_delete=models.CASCADE, to_field="number_flight", related_name="number_flight_2"
    )
    comment = models.TextField("Комментарий", null=False)
    RATE_NUMBER = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("10", "10"),
    ]
    rate = models.CharField("Оценка", max_length=2, choices=RATE_NUMBER)
    sing_author = models.CharField("Укажите ваш ник", max_length=30)
