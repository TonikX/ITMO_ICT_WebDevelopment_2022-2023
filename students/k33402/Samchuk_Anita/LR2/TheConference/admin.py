from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Conference)
admin.site.register(Tag)
admin.site.register(Participant)
admin.site.register(Performance)
admin.site.register(Comment)

