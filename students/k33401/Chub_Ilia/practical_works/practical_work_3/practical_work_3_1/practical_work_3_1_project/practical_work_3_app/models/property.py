from . import *
from .car_owner import CarOwner
from .car import Car


class Property(models.Model):
    id = models.IntegerField(primary_key=True)
    owner_id = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
