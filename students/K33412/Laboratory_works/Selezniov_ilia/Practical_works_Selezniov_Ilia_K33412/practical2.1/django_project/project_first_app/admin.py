from django.contrib import admin
from .models import Owner, OwnedCars, Car, DrivingLicense

admin.site.register(Owner)
admin.site.register(OwnedCars)
admin.site.register(Car)
admin.site.register(DrivingLicense)
