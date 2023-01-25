from django.contrib import admin
from .models import Hotel, Reservation,Room, Comment


admin.site.register(Hotel)
admin.site.register(Reservation)
admin.site.register(Room)
admin.site.register(Comment)