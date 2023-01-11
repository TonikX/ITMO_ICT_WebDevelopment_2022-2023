from django.contrib import admin
from .models import Auto, OwnerUser, Ownership, DrivingLicense

admin.site.register(Auto)
admin.site.register(OwnerUser)
admin.site.register(Ownership)
admin.site.register(DrivingLicense)
