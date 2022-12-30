from django.contrib import admin
from .models import *
admin.site.register(Conference)
admin.site.register(Registration)
admin.site.register(Comment)
admin.site.register(Recommendation)