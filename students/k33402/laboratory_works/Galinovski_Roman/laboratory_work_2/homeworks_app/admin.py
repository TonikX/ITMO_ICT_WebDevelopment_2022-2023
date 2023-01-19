from django.contrib import admin
from .models import User, Course, Homework, StudentHomework

admin.site.register(User)
admin.site.register(Homework)
admin.site.register(Course)
admin.site.register(StudentHomework)