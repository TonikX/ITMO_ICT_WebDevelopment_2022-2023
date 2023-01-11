from django.contrib import admin
from .models import Driver, Vehicle, Licence, Ownership

admin.site.register(Driver)
admin.site.register(Vehicle)
admin.site.register(Licence)
admin.site.register(Ownership)