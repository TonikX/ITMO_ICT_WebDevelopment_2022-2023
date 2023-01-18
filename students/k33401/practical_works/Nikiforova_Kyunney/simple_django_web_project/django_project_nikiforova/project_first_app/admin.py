from django.contrib import admin
from .models import Owner, Car, Ownership, DriversLicense

# Register your models here.
admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(Ownership)
admin.site.register(DriversLicense)
