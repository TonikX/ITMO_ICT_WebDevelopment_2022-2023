from django.contrib import admin

from .models import Owner, License, Ownership, Car

admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(Ownership)
admin.site.register(License)