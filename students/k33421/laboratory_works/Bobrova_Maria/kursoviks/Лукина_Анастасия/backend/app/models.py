from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from phonenumber_field.modelfields import PhoneNumberField
from smart_selects.db_fields import ChainedForeignKey


class Exhibition(models.Model):
    title = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    address = models.TextField()
    TYPES = (
        ('T1', 'Монопородная выставка'),
        ('T2', 'Полипородная выставка'),
    )
    exhibition_type = models.CharField(max_length=2, choices=TYPES)
    date_start = models.DateField()
    date_finish = models.DateField()
    image = models.ImageField(upload_to='exhibition/static')

    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Competition(models.Model):
    ring = models.IntegerField()
    ex1 = models.CharField(max_length=100)
    ex2 = models.CharField(max_length=100)
    ex3 = models.CharField(max_length=100)
    date = models.DateField()
    exhibition = models.ForeignKey(
        Exhibition,
        verbose_name="Выставка",
        on_delete=models.CASCADE)

    def __str__(self):
        return str(self.exhibition.title) + " " + str(self.date) + " " + str(self.ring) + " ринг"


class DogOwner(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    passport = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    phone = PhoneNumberField()
    email = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name) + " " + str(self.surname)


class Expert(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = PhoneNumberField()
    email = models.CharField(max_length=100)
    education = models.CharField(max_length=256)
    info = models.TextField(default = " ")

    def __str__(self):
        return str(self.name) + " " + str(self.surname)


class ExpertCompetition(models.Model):
    competition = models.ForeignKey(
        Competition,
        verbose_name="Соревнование",
        on_delete=models.CASCADE)

    expert = models.ForeignKey(
        Expert,
        verbose_name="Эксперт",
        on_delete=models.CASCADE)


class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    birth_date = models.DateField()
    owner = models.ForeignKey(
        DogOwner,
        verbose_name="Хозяин",
        on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class DogRegistration(models.Model):
    exhibition = models.ForeignKey(
        Exhibition,
        verbose_name="Выставка",
        on_delete=models.CASCADE)
    owner = models.ForeignKey(
        DogOwner,
        verbose_name="Хозяин",
        on_delete=models.CASCADE)

    dog = ChainedForeignKey(
        Dog,
        verbose_name="Собака",
        chained_field="owner",
        chained_model_field="owner",
        show_all=False,
        auto_choose=True,
        sort=True)

    # dog = models.ForeignKey(
    #     Dog,
    #     verbose_name="Собака",
    #     on_delete=models.CASCADE)

    is_paid = models.BooleanField(verbose_name="Оплата")

    def __str__(self):
        return str(self.exhibition) + " " + str(self.dog)


class CompParticipation(models.Model):
    competition = models.ForeignKey(
        Competition,
        verbose_name="Соревнование",
        on_delete=models.CASCADE)
    dog = models.ForeignKey(
        Dog,
        verbose_name="Собака",
        on_delete=models.CASCADE)

    def __str__(self):
        return str(self.competition) + " " + str(self.dog.name)


class Result(models.Model):
    expert = models.ForeignKey(
        Expert,
        verbose_name="Эксперт",
        on_delete=models.CASCADE)
    score1 = models.IntegerField()
    score2 = models.IntegerField()
    score3 = models.IntegerField()
    comp_participation = models.ForeignKey(
        CompParticipation,
        verbose_name="Участие",
        on_delete=models.CASCADE)

    def total(self):
        return self.score1 + self.score2 + self.score3


class Club(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return str(self.title)


class ClubParticipation(models.Model):
    club = models.ForeignKey(
        Club,
        verbose_name="Клуб",
        on_delete=models.CASCADE)
    dog = models.ForeignKey(
        Dog,
        verbose_name="Собака",
        on_delete=models.CASCADE)

    def __str__(self):
        return str(self.club) + " " + str(self.dog.name)


class Dismissed(models.Model):
    dog = models.ForeignKey(
        Dog,
        verbose_name="Собака",
        on_delete=models.CASCADE)

    competition = models.ForeignKey(
        Competition,
        verbose_name="Соревнование",
        on_delete=models.CASCADE)
