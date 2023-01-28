from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users_app.models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ["username", ]


admin.site.register(User, CustomUserAdmin)
