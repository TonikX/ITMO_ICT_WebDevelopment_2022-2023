from django.contrib import admin

from .models import *


@admin.register(Conference, Author, Performance)
class Admin(admin.ModelAdmin):
	pass
