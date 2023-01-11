from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CarOwner)
admin.site.register(Car)
admin.site.register(DriverLicense)
admin.site.register(Ownership)