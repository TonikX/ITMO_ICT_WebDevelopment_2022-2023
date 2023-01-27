from django.contrib import admin

from .models import *

admin.site.register(Guest)
admin.site.register(CleaningStaff)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Cleaning)
