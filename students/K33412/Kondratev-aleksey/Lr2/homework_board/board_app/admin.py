from django.contrib import admin
from .models import Homework, TaskCompletion, User

admin.site.register(Homework)
admin.site.register(TaskCompletion)
admin.site.register(User)