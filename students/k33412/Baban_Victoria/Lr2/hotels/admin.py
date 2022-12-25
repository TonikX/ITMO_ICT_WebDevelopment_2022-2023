from django.contrib import admin
from hotels.models import *

admin.site.register(Booking)
admin.site.register(Hotel)
admin.site.register(Guest)
admin.site.register(Feedback)
admin.site.register(Room)