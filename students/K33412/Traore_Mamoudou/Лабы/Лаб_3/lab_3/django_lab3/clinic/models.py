from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

SEXES = [
    ('Мужчина', 'Мужчина'),
    ('Женщина', 'Женщина')
]

APPOINTMENT_TYPES = [
    ('Консультация', 'Консультация'),
    ('Осмотр', 'Осмотр'),
    ('Сдача анализов', 'Сдача анализов'),
]

WEEK_DAYS = [
    ('пн', 'Понедельник'),
    ('вт', 'Вторник'),
    ('ср', 'Среда'),
    ('чт', 'Четверг'),
    ('пт', 'Пятница'),
    ('сб', 'Суббота'),
    ('вс', 'Воскресенье')
]


PAYMENTS = [
    ('Банковская карта', 'Банковская карта'),
    ('Наличные', 'Наличные')
]


class Doctor(AbstractUser):

    username = models.CharField(max_length=20, unique=True)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    specialty = models.CharField(max_length=30, default='Терапевт')
    education = models.CharField(max_length=40, default='Университет ITMO')
    sex = models.CharField(max_length=7, choices=SEXES, default='Мужчина')
    date_of_birth = models.DateField(default='2000-01-01')
    start_work_date = models.DateField(auto_now_add=True)
    finish_work_date = models.DateField(blank=True, null=True)
    contract_number = models.IntegerField(blank=True, null=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'middle_name', 'specialty', 'education', 'sex', 'date_of_birth', 'contract_number']

    def __str__(self):
        string = f'{self.last_name} {self.first_name[0]}.'
        if self.middle_name:
            string += f'{self.middle_name[0]}.'
        return string


class Patient(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    sex = models.CharField(max_length=7, choices=SEXES, default='Мужчина')
    date_of_birth = models.DateField()

    def __str__(self):
        string = f'{self.last_name} {self.first_name[0]}.'
        if self.middle_name:
            string += f'{self.middle_name[0]}.'
        return string


class AppointmentType(models.Model):

    title = models.CharField(max_length=15, choices=APPOINTMENT_TYPES)
    price = models.IntegerField(default=1000)

    def __str__(self):
        return f'{self.title} - {self.price}p'


class Cabinet(models.Model):

    number = models.IntegerField(unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    patients = models.ManyToManyField(Patient, through='Appointment', related_name='cabinets')
    doctors = models.ManyToManyField(Doctor, through='Timetable', related_name='cabinets')

    def __str__(self):
        return str(self.number)


class Appointment(models.Model):

    cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    finish_time = models.DateTimeField(blank=True, null=True)
    start_time = models.DateTimeField()
    type = models.ForeignKey(AppointmentType, on_delete=models.CASCADE)
    diagnosis = models.CharField(max_length=30, blank=True, null=True)
    health_status = models.TextField(blank=True, null=True)
    recommendations = models.TextField(blank=True, null=True)
    payed = models.BooleanField(default=False)
    form_of_payment = models.CharField(max_length=16, choices=PAYMENTS, default='Наличные')

    def __str__(self):
        return f'{self.patient} - {self.cabinet} ({self.start_time})'


class Timetable(models.Model):

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='timetable')
    cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE, related_name='timetable')
    week_day = models.CharField(max_length=2, choices=WEEK_DAYS)

    def __str__(self):
        return f'{self.doctor} - {self.cabinet} ({self.week_day})'