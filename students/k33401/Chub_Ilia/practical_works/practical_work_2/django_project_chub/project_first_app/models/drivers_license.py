from . import *
from .car_owner import CarOwner


class DriversLicense(models.Model):
    id = models.IntegerField(primary_key=True)
    owner_id = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10, null=False)
    type = models.CharField(max_length=10, null=False)
    date_of_license = models.DateField()
