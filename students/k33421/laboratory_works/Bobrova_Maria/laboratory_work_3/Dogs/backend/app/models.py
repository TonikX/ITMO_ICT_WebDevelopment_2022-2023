from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from phonenumber_field.modelfields import PhoneNumberField
from smart_selects.db_fields import ChainedForeignKey


class Show(models.Model):
    title = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    address = models.TextField()
    TYPES = (
        ('T1', 'Монопородная выставка'),
        ('T2', 'Полипородная выставка'),
    )
    show_type = models.CharField(max_length=2, choices=TYPES)
    date_start = models.DateField()
    date_finish = models.DateField()

    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Ring(models.Model):
    ring = models.IntegerField()
    ex1 = models.CharField(max_length=100)
    ex2 = models.CharField(max_length=100)
    ex3 = models.CharField(max_length=100)
    date = models.DateField()
    show = models.ForeignKey(
        Show,
        verbose_name="Выставка",
        on_delete=models.CASCADE)

    def __str__(self):
        return str(self.show.title) + " " + str(self.date) + " " + str(self.ring) + " ринг"



class Expert(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = PhoneNumberField()
    email = models.CharField(max_length=100)
    education = models.CharField(max_length=256)
    info = models.TextField(default = " ")
    show = models.ForeignKey(
        Show,
        verbose_name="Выставка",
        on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name) + " " + str(self.surname)



class Participant(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    birth_date = models.DateField()
    family = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Participation(models.Model):
    ring = models.ForeignKey(
        Ring,
        verbose_name="Соревнование",
        on_delete=models.CASCADE)

    VACCINATED = (
        ('Y', 'Да'),
        ('N', 'Нет'),
    )
    vaccinated = models.CharField(max_length=3, choices=VACCINATED)
    dismissed = models.CharField(max_length=100)
    final_grade = models.IntegerField(max_length=100)
    MEDAL = (
        ('З', 'Золото'),
        ('С', 'Серебро'),
        ('Б', 'Бронза')
    )
    medal = models.CharField(max_length=20, choices=MEDAL)

    def __str__(self):
        return str(self.ring)

class Club(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return str(self.title)




