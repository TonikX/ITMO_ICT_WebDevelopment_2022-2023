from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Event)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(UserEventEnrollment)
