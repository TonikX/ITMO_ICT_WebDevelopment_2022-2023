from django.contrib import admin

# Register your models here.
from .models import Motorist, License, Automobile, Ownership

admin.site.register(Motorist)
admin.site.register(License)
admin.site.register(Automobile)
admin.site.register(Ownership)
