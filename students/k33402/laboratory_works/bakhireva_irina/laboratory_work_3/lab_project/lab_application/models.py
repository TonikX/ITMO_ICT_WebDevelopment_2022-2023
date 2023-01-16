from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

EDUCATION_MIDDLE = 1
EDUCATION_HIGH = 2
EDUCATION_BACHELOR = 3
EDUCATION_MASTER = 4
EDUCATION_LEVEL_CHOICES = (
	(EDUCATION_MIDDLE, 'Middle'),
	(EDUCATION_HIGH, 'High'),
	(EDUCATION_BACHELOR, 'Bachelor'),
	(EDUCATION_MASTER, 'Master'),
)

ROLE_APPLICANT = 1
ROLE_HR = 2
ROLE_CHOICES = (
	(ROLE_APPLICANT, 'Applicant'),
	(ROLE_HR, 'HR'),
)


class User(AbstractUser):
	REQUIRED_FIELDS = ["first_name", "last_name", "phone", "email"]

	role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=ROLE_APPLICANT, null=True)
	phone = models.TextField()


class Specialization(models.Model):
	name = models.TextField()
	level = models.IntegerField()
	level_name = models.TextField(null=True)


class Course(models.Model):
	name = models.TextField()
	spec = models.ForeignKey(Specialization, on_delete=models.CASCADE, related_name="courses")
	required_spec = models.ForeignKey(Specialization, on_delete=models.CASCADE, null=True)
	description = models.TextField()


# Соискатель

class Applicant(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="applicant")


class ApplicantHistory(models.Model):
	applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name="work_history")
	spec = models.ForeignKey(Specialization, on_delete=models.CASCADE,
	                         null=True)  # Если нет специализации, то это пособие
	salary = models.PositiveIntegerField()
	start_date = models.DateTimeField()
	end_date = models.DateTimeField(null=True)


class ApplicantEducation(models.Model):
	applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name="education")
	education_level = models.PositiveSmallIntegerField(choices=EDUCATION_LEVEL_CHOICES)
	description = models.TextField()
	start_date = models.DateTimeField()
	end_date = models.DateTimeField(null=True)


class ApplicantCourses(models.Model):
	applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name="courses")
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField(null=True)


# Компания

class HR(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="hr")


class Company(models.Model):
	name = models.TextField()
	address = models.TextField()
	hr = models.ForeignKey(HR, on_delete=models.CASCADE, related_name="company")


# Вакансия

class Vacancy(models.Model):
	company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")

	education_level = models.PositiveSmallIntegerField(choices=EDUCATION_LEVEL_CHOICES)
	seniority = models.TextField()
	salary = models.PositiveIntegerField()
	description = models.TextField()
	specs = models.ManyToManyField(Specialization, through="RequiredVacancySpecialization")

	created_date = models.DateTimeField(default=timezone.now, null=True)
	closed_date = models.DateTimeField(null=True)


class RequiredVacancySpecialization(models.Model):
	vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
	spec = models.ForeignKey(Specialization, on_delete=models.CASCADE)
