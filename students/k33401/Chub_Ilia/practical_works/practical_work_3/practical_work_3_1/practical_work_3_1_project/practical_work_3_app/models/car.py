from . import *


class Car(models.Model):
    id = models.IntegerField(primary_key=True)
    state_number = models.CharField(max_length=15, null=False)
    brand = models.CharField(max_length=20, null=False)
    model = models.CharField(max_length=20, null=False)
    color = models.CharField(max_length=30, null=True)