from django.contrib import admin
from .models import Owner, License, Car, Property


@admin.register(Owner, License, Car, Property)
class Admin(admin.ModelAdmin):
    pass
