from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Student, User, Teacher, StudentGroup, Homework, HomeworkAnswer, TeacherAnswerOnHomework

admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(StudentGroup)
admin.site.register(Homework)
admin.site.register(HomeworkAnswer)
admin.site.register(TeacherAnswerOnHomework)
