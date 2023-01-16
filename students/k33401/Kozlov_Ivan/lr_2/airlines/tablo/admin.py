from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *

admin.site.register(Registration_user, UserAdmin)
admin.site.register(Flight)
admin.site.register(Ticket)
admin.site.register(Review)
