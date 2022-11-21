from django.contrib import admin
from .models import Owner
from .models import Car

# Register your models here.

admin.site.register(Owner)
admin.site.register(Car)
