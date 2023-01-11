from django.contrib import admin
from .models import Car, Owner, Ownership, DriverLicense

admin.site.register([Car, Owner, Ownership, DriverLicense])
