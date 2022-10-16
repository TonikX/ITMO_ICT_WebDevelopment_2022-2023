from django.contrib import admin

from timetable.models import Student, User, Teacher, StudentGroup, Homework, HomeworkAnswer

admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(StudentGroup)
admin.site.register(Homework)
admin.site.register(HomeworkAnswer)