from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class UserRacer(AbstractUser):
    first_name = models.CharField("First name", max_length=30)
    last_name = models.CharField("Last name", max_length=30)
    patronymic = models.CharField("Patronymic", null=True, max_length=30)
    team = models.CharField("Team", null=True, max_length=30)
    member_descr = models.TextField("Team member description", null=True)
    car_descr = models.TextField("Car description", null=True)
    experience_years = models.IntegerField("Experience in years", null=True)
    CLASSES = [ ('C', 'Non-pro'),
                ('B', 'Experienced'),
                ('A', 'Professional'),
                ('L', 'Another')]
    user_class = models.CharField("User's class", max_length=30, choices=CLASSES, default='L')
    username = models.CharField("Username", primary_key=True, max_length=50)
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Race(models.Model):
    num_race = models.AutoField("Race number", primary_key=True)
    name_race = models.CharField("Race name", max_length=50)
    date_race = models.DateTimeField("Race date", unique=True)
    place_race = models.CharField("Race place", max_length=50)

    first_place = models.ForeignKey("UserRacer", on_delete=models.CASCADE, null=True, blank=True)
    second_place = models.ForeignKey("UserRacer", on_delete=models.CASCADE, null=True, blank=True, related_name='sec_place')
    third_place = models.ForeignKey("UserRacer", on_delete=models.CASCADE, null=True, blank=True, related_name='th_pace')

    def __str__(self):
        return f"Race: {self.num_race}, {self.name_race}"


class Registration(models.Model):
    num_reg = models.AutoField("Registration number", primary_key=True)
    num_race_reg = models.ForeignKey(Race, on_delete=models.CASCADE)
    num_user_reg = models.ForeignKey(UserRacer, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.num_reg}, user: {self.num_user_reg}")


class Comment(models.Model):
    id_review = models.AutoField(primary_key=True)
    num_race =  models.ForeignKey(Race, on_delete=models.CASCADE)
    time_race = models.DateTimeField("Race date and time")
    comment_time = models.DateTimeField(default=datetime.now(), blank=True)

    COMMENT_TYPES = [('RACE_Q', 'Question about race'),
                     ('COLLAB_Q', 'Question about collaboration'),
                     ('OTHER', 'Other')]
    rate = models.IntegerField("Rating", default=10, validators=[MaxValueValidator(10), MinValueValidator(1)],
                               null=True, blank=True)
    username = models.ForeignKey(UserRacer, on_delete=models.CASCADE)
    comment_type = models.CharField("Comment type", max_length=30, choices=COMMENT_TYPES)
    text = models.TextField("Comment")

    def save(self, *args, **kwargs):
        self.time_race = self.num_race.date_race
        super(Comment, self).save(*args, **kwargs)