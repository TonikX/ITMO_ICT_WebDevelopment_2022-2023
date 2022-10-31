from django.contrib import admin
from .models import Hotel, Room, Booking, Review

admin.site.register([Hotel, Room, Booking, Review])
