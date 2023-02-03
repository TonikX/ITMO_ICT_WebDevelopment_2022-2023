from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Car(models.Model):
    BRAND_CAR = (('RENAULT', 'Renault'), ('VOLKSWAGEN', 'Volkswagen'), ('KIA', 'Kia'), ('SKODA', 'Skoda'), ('TOYOTA', 'Toyota'), ('PEUGEOT', 'Peugeot'))
    reg_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20, choices=BRAND_CAR)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True)
    def __str__(self):
        return "{} {} {} {}".format(self.reg_number, self.brand, self.model, self.color)

class Owner(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateField(null=True)
    passport = models.IntegerField(null=True)
    address = models.CharField(max_length=100, null=True)
    nationality = models.CharField(max_length=30, null=True)
    case = models.ManyToManyField(Car, through='Owning')

    def __str__(self):
        return "{} {} {} {} {} {}".format(self.first_name, self.last_name, self.birthdate, self.passport, self.address, self.nationality)

class License(models.Model):
    TYPE_L = (('M', 'm'), ('A', 'a'), ('B', 'b'), ('BE', 'be'), ('C', 'c'), ('CE', 'ce'), ('D', 'd'), ('DE', 'de'), ('TM', 'tm'), ('TB', 'tb'))
    owner_id = models.ForeignKey(Owner, on_delete=models.DO_NOTHING)
    num_license = models.CharField(max_length=10)
    type_license = models.CharField(max_length=10, choices=TYPE_L)
    date_license = models.DateField()

class Owning(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.DO_NOTHING)
    car_id = models.ForeignKey(Car, on_delete=models.DO_NOTHING)
    date_start = models.DateField()
    date_fin = models.DateField(null=True)