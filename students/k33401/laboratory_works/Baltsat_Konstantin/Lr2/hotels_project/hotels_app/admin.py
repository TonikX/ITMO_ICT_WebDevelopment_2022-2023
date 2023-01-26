from django.contrib import admin

# Register your models here.
from .models import Hotel, Room, Booking, Review

admin.site.register([Hotel, Room, Booking, Review])