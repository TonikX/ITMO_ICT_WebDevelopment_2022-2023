from django.contrib import admin

from . import models

admin.site.register(models.User)
admin.site.register(models.Ticket)


# admin.site.register(models.Flight)
class FlightAdmin(admin.ModelAdmin):
    # readonly_fields = ('reservations',)
    pass


admin.site.register(models.Flight, FlightAdmin)
