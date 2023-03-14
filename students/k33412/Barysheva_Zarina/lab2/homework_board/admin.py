from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Subject)
admin.site.register(Assignment)
admin.site.register(DoneTask)
