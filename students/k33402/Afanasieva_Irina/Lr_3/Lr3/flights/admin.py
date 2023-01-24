from django.contrib import admin
from flights.models import *


admin.site.register(Flight)
admin.site.register(Ticket)
admin.site.register(Plane)
admin.site.register(Passenger)
admin.site.register(AirCompany)