from django.db import models


# Create your models here.
class Car(models.Model):
    state_number = models.CharField(max_length=15, null=False)
    make_car = models.CharField(max_length=20, null=False)
    model_car = models.CharField(max_length=20, null=False)
    colour = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.id.__str__()


class CarOwner(models.Model):
    lastname = models.CharField(max_length=30, null=False)
    first_name = models.CharField(max_length=30, null=False)
    birthday = models.DateField()
    cars = models.ManyToManyField(Car, through='Ownership')

    def __str__(self):
        return self.id.__str__()


class Ownership(models.Model):
    id_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    id_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    expiration_date = models.DateField(null=True)

    def __str__(self):
        return "{}_{}".format(self.id_owner.__str__(), self.id_car.__str__())


class DriverLicense(models.Model):
    id_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10, null=False)
    type = models.CharField(max_length=10, null=False)
    date_of_license = models.DateField()
