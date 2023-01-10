from django.contrib import admin
from .models import Car_owner, Car, Driver_license, Ownerdhip
# Register your models here.

admin.site.register(Car)
admin.site.register(Car_owner)
admin.site.register(Driver_license)
admin.site.register(Ownerdhip)