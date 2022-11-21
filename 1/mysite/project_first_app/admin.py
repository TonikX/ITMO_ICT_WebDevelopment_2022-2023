from django.contrib import admin
from .models import CarOwner
from .models import Vehicle

# Register your models here.

admin.site.register(CarOwner)
admin.site.register(Vehicle)
