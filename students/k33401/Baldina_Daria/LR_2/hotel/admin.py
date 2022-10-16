from django.contrib import admin
from .models import Hotel, Reservation,Room, Guest, Comment
# Register your models here.

admin.site.register(Hotel)
admin.site.register(Reservation)
admin.site.register(Room)
admin.site.register(Guest)
admin.site.register(Comment)