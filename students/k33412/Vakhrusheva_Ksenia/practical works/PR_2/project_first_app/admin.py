from django.contrib import admin

from .models import Owner, License, Vehicle, Property


@admin.register(Owner, License, Vehicle, Property)
class Admin(admin.ModelAdmin):
	pass
