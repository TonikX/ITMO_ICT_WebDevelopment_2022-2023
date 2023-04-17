from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Motorist(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birth = models.DateField()



class License(models.Model):
    TYPES = models.TextChoices('TYPES', 'A B A1 C D E F M BE CE DE')
    motorist = models.ForeignKey(Motorist, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    license_type = models.CharField(choices=TYPES.choices, max_length=3)
    given = models.DateField()


class Automobile(models.Model):
    gos_number = models.CharField(max_length=15)
    mark = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(blank=True, max_length=30)
    owning = models.ManyToManyField(Motorist, through='Ownership')

    def __str__(self):
        return "{} {} {} {}".format(self.gos_number, self.mark, self.model, self.color)


class Ownership(models.Model):
    id_auto = models.ForeignKey(Automobile, on_delete=models.CASCADE)
    id_motorist = models.ForeignKey(Motorist, on_delete=models.CASCADE)
    begin = models.DateField()
    end = models.DateField(blank=True, null=True)
