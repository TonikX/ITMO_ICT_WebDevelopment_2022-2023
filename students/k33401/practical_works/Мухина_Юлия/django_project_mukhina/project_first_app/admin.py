from django.contrib import admin
from .models import OwnerUser, Ownership, Car, License
# Register your models here.

admin.site.register(OwnerUser)
admin.site.register(Ownership)
admin.site.register(Car)
admin.site.register(License)