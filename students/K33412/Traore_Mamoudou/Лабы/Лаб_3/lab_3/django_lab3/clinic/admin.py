from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(AppointmentType)
admin.site.register(Cabinet)
admin.site.register(Appointment)
admin.site.register(Timetable)