from django.contrib import admin

from avto.models import Car_owner, Car, Ownership, Drivers_license, User

admin.site.register(Car_owner)
admin.site.register(Car)
admin.site.register(Ownership)
admin.site.register(Drivers_license)
admin.site.register(User)