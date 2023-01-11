from django.contrib import admin
from .models import Guest, Hotel, Room, Accommodation, Comment

admin.site.register(Guest)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Accommodation)
admin.site.register(Comment)
