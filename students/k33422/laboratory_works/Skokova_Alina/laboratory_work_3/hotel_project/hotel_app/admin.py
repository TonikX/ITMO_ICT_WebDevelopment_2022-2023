from django.contrib import admin

from .models import *

admin.site.register(Room)
admin.site.register(Price)
admin.site.register(Client)
admin.site.register(Booking)
admin.site.register(Cleaner)
admin.site.register(Floor)
admin.site.register(Schedule)