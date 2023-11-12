from django.contrib import admin
from .models import Owner, Hotel, RoomType, Facilities, Room, Reservation, Comment

admin.site.register(Owner)
admin.site.register(Hotel)
admin.site.register(RoomType)
admin.site.register(Facilities)
admin.site.register(Room)
admin.site.register(Reservation)
admin.site.register(Comment)
