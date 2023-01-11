from django.contrib import admin
from backend.profiles.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    """Профиль"""
    list_display = ("user", "nike", "id")

admin.site.register(Profile, ProfileAdmin)
