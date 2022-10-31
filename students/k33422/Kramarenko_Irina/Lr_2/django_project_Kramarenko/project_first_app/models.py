from django.db import models

# Create your models here.
class Car(models.Model):
    BRAND_CAR = (('RENAULT', 'Renault'), ('VOLKSWAGEN', 'Volkswagen'), ('KIA', 'Kia'), ('SKODA', 'Skoda'), ('TOYOTA', 'Toyota'), ('PEUGEOT', 'Peugeot'))
    # car_id = models.IntegerField(primary_key=True)
    reg_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20, choices=BRAND_CAR)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True)

class Owner(models.Model):
    # owner_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateField(null=True)
    case = models.ManyToManyField(Car, through='Owning')

class License(models.Model):
    TYPE_L = (('M', 'm'), ('A', 'a'), ('B', 'b'), ('BE', 'be'), ('C', 'c'), ('CE', 'ce'), ('D', 'd'), ('DE', 'de'), ('TM', 'tm'), ('TB', 'tb'))
    # license_id = models.IntegerField(primary_key=True)
    owner_id = models.ForeignKey(Owner, on_delete=models.DO_NOTHING)
    num_license = models.CharField(max_length=10)
    type_license = models.CharField(max_length=10, choices=TYPE_L)
    date_license = models.DateField()

class Owning(models.Model):
    # owning_id = models.IntegerField(primary_key=True)
    owner_id = models.ForeignKey(Owner, on_delete=models.DO_NOTHING)
    car_id = models.ForeignKey(Car, on_delete=models.DO_NOTHING)
    date_start = models.DateField()
    date_fin = models.DateField(null=True)