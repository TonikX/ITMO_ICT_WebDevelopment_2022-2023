from django.contrib import admin

from . import models
from . import forms

admin.site.register(models.User)
admin.site.register(models.Library)
admin.site.register(models.ReadingRoom)
admin.site.register(models.Book)
admin.site.register(models.BookUser)


# @admin.register(models.Flight)
# class FlightAdmin(admin.ModelAdmin):
#     form = forms.FlightValidationForm
