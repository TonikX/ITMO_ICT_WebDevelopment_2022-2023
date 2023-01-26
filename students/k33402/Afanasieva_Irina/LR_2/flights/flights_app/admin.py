from django.contrib import admin

from .models import User, Flight, Reservation, Review

admin.site.register(User)
admin.site.register(Flight)
admin.site.register(Reservation)
admin.site.register(Review)
