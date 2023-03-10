from django.contrib import admin

from . import models
from . import forms

admin.site.register(models.Library)


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    form = forms.UserValidationForm


@admin.register(models.ReadingRoom)
class ReadingRoomAdmin(admin.ModelAdmin):
    form = forms.ReadingRoomValidationForm


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    form = forms.BookValidationForm


@admin.register(models.ReadingRoomBook)
class ReadingRoomBookAdmin(admin.ModelAdmin):
    form = forms.ReadingRoomBookValidationForm


@admin.register(models.ReadingRoomBookUser)
class ReadingRoomBookUserAdmin(admin.ModelAdmin):
    form = forms.ReadingRoomBookUserValidationForm
