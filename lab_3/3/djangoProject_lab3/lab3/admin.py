from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Driver)
admin.site.register(Car)
admin.site.register(License)
admin.site.register(Owner)
