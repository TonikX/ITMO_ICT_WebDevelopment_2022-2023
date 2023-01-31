from django.contrib import admin
from tourism.models import Tour, Tourist, Reservation

@admin.register(Tour, Tourist, Reservation)
class Admin(admin.ModelAdmin):
    pass