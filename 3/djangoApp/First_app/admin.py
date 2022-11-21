from django.contrib import admin
from .models import Owner_Model
from .models import Car_Model

# Register your models here.

admin.site.register(Owner_Model)
admin.site.register(Car_Model)
