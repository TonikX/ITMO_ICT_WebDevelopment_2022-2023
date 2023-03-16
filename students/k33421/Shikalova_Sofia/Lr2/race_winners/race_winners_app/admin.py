from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserRacer)
admin.site.register(Race)
admin.site.register(Registration)
admin.site.register(Comment)