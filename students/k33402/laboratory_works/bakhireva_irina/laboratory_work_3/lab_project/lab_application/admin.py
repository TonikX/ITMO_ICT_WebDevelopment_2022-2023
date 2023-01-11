from django.contrib import admin

from lab_application.models import *


# Register your models here.

@admin.register(User, Specialization, Course, Applicant, ApplicantHistory, ApplicantEducation, ApplicantCourses, HR,
                Company, Vacancy, RequiredVacancySpecialization)
class Admin(admin.ModelAdmin):
	pass
