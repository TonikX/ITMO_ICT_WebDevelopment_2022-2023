from django.contrib import admin
from .models import CarOwner, Car, DriverLicense, OwnerShip


admin.site.register(Car)
admin.site.register(CarOwner)
admin.site.register(DriverLicense)
admin.site.register(OwnerShip)