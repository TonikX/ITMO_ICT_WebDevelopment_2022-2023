from django.contrib import admin

from . import models
from . import forms

admin.site.register(models.User)
admin.site.register(models.Review)


@admin.register(models.Flight)
class FlightAdmin(admin.ModelAdmin):
    form = forms.FlightValidationForm
