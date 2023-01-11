from django.db import models

class Owner(models.Model):
    owner_id = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=30, null=False)
    first_name = models.CharField(max_length=30, null=False)
    birthday = models.DateField()


class Car(models.Model):
    car_id = models.IntegerField(primary_key=True)
    state_num = models.CharField(max_length=15, null=False)
    brand = models.CharField(max_length=20, null=False)
    model = models.CharField(max_length=20, null=False)
    color = models.CharField(max_length=30, null=True)


class Ownership(models.Model):
    owner_car_id = models.IntegerField(primary_key=True)
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='owner')
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car')
    start_date = models.DateField()
    end_date = models.DateField(null=True)


class License(models.Model):
    license_id = models.IntegerField(primary_key=True)
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='car_owner')
    license_num = models.CharField(max_length=10, null=False)
    type = models.CharField(max_length=10, null=False)
    start_date_license = models.DateField()
