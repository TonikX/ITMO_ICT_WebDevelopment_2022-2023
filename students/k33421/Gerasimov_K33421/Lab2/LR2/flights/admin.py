from django.contrib import admin
from .models import AviaCompany, Flight, Booking

admin.site.register(AviaCompany)
admin.site.register(Flight)
admin.site.register(Booking)
