from project_first_app.models import *
import random

Car.objects.filter(brand="Renault")

CarOwner.objects.filter(first_name="Ivan")

DrivingLicense.objects.get(id_owner=random.choice(CarOwner.objects.all()).id_owner)

CarOwner.objects.filter(owner_ownership__id_car__color="red")

CarOwner.objects.filter(owner_ownership__date_of_start__gt="2009-01-01")
