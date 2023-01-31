from django.contrib import admin

# Register your models here.
from apps.groups.models import Group


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'teacher')
    list_filter = ('subject', 'teacher')


admin.site.register(Group, GroupAdmin)
