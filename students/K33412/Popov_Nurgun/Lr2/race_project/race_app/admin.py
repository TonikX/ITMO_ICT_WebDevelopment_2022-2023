from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Racer)
admin.site.register(Car)
admin.site.register(Race)
admin.site.register(Registration)
admin.site.register(Comment)