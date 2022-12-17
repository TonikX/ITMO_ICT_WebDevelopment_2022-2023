from django.contrib import admin

from users_app.models import User


class CleaningStaffAdmin(admin.ModelAdmin):
    list_filter = ("is_cleaning_staff", "is_superuser")


admin.site.register(User, CleaningStaffAdmin)
