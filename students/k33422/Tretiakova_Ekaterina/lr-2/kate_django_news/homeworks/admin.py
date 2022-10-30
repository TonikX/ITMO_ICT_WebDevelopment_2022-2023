from django.contrib import admin

from homeworks.models import User, Subject, Grade, Homework

# Register your models here.
admin.site.register(Grade)
admin.site.register(Subject)
admin.site.register(User)
admin.site.register(Homework)


