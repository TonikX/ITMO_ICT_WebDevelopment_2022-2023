from django.contrib import admin
from .models import Passenger, Airline, Flight, Ticket, Comment

admin.site.register(Passenger)
admin.site.register(Airline)
admin.site.register(Flight)
admin.site.register(Ticket)
admin.site.register(Comment)
