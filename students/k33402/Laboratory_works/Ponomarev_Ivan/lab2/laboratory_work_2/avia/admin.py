from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Flight)
admin.site.register(Ticket)
admin.site.register(Plane)
admin.site.register(Comment)
