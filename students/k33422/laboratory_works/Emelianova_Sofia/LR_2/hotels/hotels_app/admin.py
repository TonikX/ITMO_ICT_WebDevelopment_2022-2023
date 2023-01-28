from django.contrib import admin

from .models import User, Hotel, Reservation, Review

admin.site.register(User)
admin.site.register(Hotel)
admin.site.register(Reservation)
admin.site.register(Review)
