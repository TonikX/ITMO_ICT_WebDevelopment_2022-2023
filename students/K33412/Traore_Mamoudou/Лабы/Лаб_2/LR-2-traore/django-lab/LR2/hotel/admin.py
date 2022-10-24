from django.contrib import admin
from .models import *

admin.site.register(Client)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Review)