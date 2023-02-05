from django.contrib import admin

from rooms_app.models import Hotel, Room, Reservation, Comment

admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Reservation)
admin.site.register(Comment)
