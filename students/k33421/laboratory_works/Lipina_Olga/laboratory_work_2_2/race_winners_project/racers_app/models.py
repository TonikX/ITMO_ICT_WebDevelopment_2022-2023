from datetime import datetime

from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
# from race_winners_project.race_winners_project.settings import AUTH_USER_MODEL

# Create your models here.
class Racer(AbstractUser):
    first_name = models.CharField("Имя", max_length=30)
    last_name = models.CharField("Фамилия", max_length=30)
    fathername = models.CharField("Отчество", null=True, blank=True, max_length=30)
    team_name = models.CharField("Название команды", null=True, blank=True, max_length=30)
    user_descr = models.TextField("Описание участника", null=True, blank=True)
    car_descr = models.TextField("Описание машины", null=True, blank=True)
    experience = models.IntegerField("Опыт", null=True, blank=True)
    USER_TYPE = [    ('A', 'Высший'),
                     ('B', 'Высокий'),
                     ('C', 'Иное')]
    type_user = models.CharField("Класс участника", max_length=30, choices=USER_TYPE, default='C')
    username = models.CharField("Логин", primary_key=True, max_length=50)
    REQUIRED_FIELDS = ['first_name', 'last_name']

    # class Meta(AbstractUser.Meta):
    #     swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return f"{self.last_name} {self.first_name}"



class Race(models.Model):
    num_race = models.AutoField("Номер гонки", primary_key=True)
    name_race = models.CharField("Название гонки", max_length=50)

    date_race = models.DateTimeField("Дата и время гонки", unique=True)
    place_race = models.CharField("Место гонки", max_length=50)

    first_place = models.ForeignKey('Racer', on_delete=models.CASCADE, null=True, blank=True)
    second_place = models.ForeignKey('Racer', on_delete=models.CASCADE, null=True, blank=True, related_name='sec_place')
    third_place = models.ForeignKey('Racer', on_delete=models.CASCADE, null=True, blank=True, related_name='th_pace')

    def __str__(self):
        return f"Гонка № {self.num_race}, {self.name_race}"


class RegistrationRace(models.Model):
    num_reg = models.AutoField("Номер регистрации", primary_key=True)
    num_race_reg = models.ForeignKey(Race, on_delete=models.CASCADE)
    num_user_reg = models.ForeignKey('Racer', on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.num_race_reg}, user: {self.num_user_reg}")

class Comment(models.Model):
    id_review = models.AutoField(primary_key=True)
    num_race =  models.ForeignKey(Race, on_delete=models.CASCADE)
    time_race = models.DateTimeField("Дата и время заезда")
    comment_time = models.DateTimeField(default=datetime.now(), blank=True)

    COMMENT_TYPES = [('RACE_Q', 'Вопрос о гонке'),
                     ('COLLAB_Q', 'Вопрос о сотрудничестве'),
                     ('OTHER', 'Иное')]
    rate = models.IntegerField("Поставьте рейтинг", default=10, validators=[MaxValueValidator(10), MinValueValidator(1)],
                               null=True, blank=True)
    username = models.ForeignKey('Racer', on_delete=models.CASCADE)
    type_comment = models.CharField("Тип комментария", max_length=30, choices=COMMENT_TYPES)
    text = models.TextField("Комментарий к гонке")

    def save(self, *args, **kwargs):
        self.time_race = self.num_race.date_race
        super(Comment, self).save(*args, **kwargs)