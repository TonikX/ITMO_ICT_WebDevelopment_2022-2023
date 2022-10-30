from django.contrib import admin
from .models import User, Hotel, Room, Reservation, Review

admin.site.register(User)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Reservation)
admin.site.register(Review)
