from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Employee)
admin.site.register(Airplane)
admin.site.register(FlightAsScheduled)
admin.site.register(Transit)
admin.site.register(AirlineAdministration)
admin.site.register(Flight)