from django.contrib import admin

# Register your models here.
from .models import Car, Ownership, CarOwner, DriverLicense

admin.site.register(Car)
admin.site.register(CarOwner)
admin.site.register(Ownership)
admin.site.register(DriverLicense)
