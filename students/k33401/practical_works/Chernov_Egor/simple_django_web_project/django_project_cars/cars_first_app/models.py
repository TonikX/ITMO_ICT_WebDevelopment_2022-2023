from django.db import models


class Driver(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return "{}. {} {}, {}".format(self.pk, self.first_name, self.last_name, self.birthday)


class DriverLicense(models.Model):
    id_driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    issue_date = models.DateField()


class Car(models.Model):
    owners = models.ManyToManyField(Driver, through='Ownership')
    license_plate = models.CharField(max_length=15)
    car_brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return "{}. {} {}, {}".format(self.pk, self.car_brand, self.model, self.license_plate, self.color)


class Ownership(models.Model):
    id_driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    id_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=True, blank=True)
