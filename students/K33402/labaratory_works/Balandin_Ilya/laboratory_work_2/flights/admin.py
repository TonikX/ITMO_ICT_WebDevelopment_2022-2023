from django.contrib import admin

from .models import *

admin.site.register(City)
admin.site.register(Airline)
admin.site.register(Flight)
admin.site.register(Ticket)
