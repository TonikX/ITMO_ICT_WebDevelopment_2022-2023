from django.contrib import admin

from work_space.models import CreateTask, AnswerTask


class CreateTaskAdmin(admin.ModelAdmin):
    list_display = (
        'teacher',
        'subject',
        'task',
    )
    search_fields = ('subject',)
    list_filter = ('teacher',)
    empty_value_display = '-пусто-'


class AnswerTaskAdmin(admin.ModelAdmin):
    list_display = (
        'task',
        'student',
        'answer',
        'date',
        'assessment',
    )
    search_fields = ('student',)
    list_filter = ('date',)
    empty_value_display = '-пусто-'


admin.site.register(CreateTask, CreateTaskAdmin)
admin.site.register(AnswerTask, AnswerTaskAdmin)
