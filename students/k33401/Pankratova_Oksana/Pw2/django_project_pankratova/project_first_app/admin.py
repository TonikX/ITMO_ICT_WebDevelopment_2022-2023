from django.contrib import admin

# Register your models here.
from .models import License, Automobile, Ownership, CustomUser

# admin.site.register(Motorist)
admin.site.register(License)
admin.site.register(Automobile)
admin.site.register(Ownership)
admin.site.register(CustomUser)
