from django.contrib import admin

from . import models
from . import forms

admin.site.register(models.User)
admin.site.register(models.Ticket)


@admin.register(models.Flight)
class FlightAdmin(admin.ModelAdmin):
    form = forms.FlightValidationForm
    # readonly_fields = ('reservations',)
