from django.contrib import admin

# Register your models here.
from apps.homeworks.models import Homework


class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'date_start', 'date_end')
    list_filter = ('group',)


admin.site.register(Homework, HomeworkAdmin)
