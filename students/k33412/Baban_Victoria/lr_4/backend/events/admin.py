from django.contrib import admin
from .models import *

admin.site.register(Event)
admin.site.register(User)
admin.site.register(UsersEvents)