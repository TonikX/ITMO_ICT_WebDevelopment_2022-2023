from django.contrib import admin
from .models import Student, StudentHomework, TeacherHomework

# Register your models here.
admin.site.register(Student)
admin.site.register(TeacherHomework)
admin.site.register(StudentHomework)