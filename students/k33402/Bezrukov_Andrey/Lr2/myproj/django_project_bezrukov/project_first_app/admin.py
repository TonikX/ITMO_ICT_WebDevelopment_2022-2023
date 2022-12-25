from django.contrib import admin
from .models import CarOwnerUser, Ownership, Car, DriversLicense
# Register your models here.

admin.site.register(CarOwnerUser)
admin.site.register(Ownership)
admin.site.register(Car)
admin.site.register(DriversLicense)


