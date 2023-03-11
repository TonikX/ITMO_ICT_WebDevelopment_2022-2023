from django.contrib import admin

from .models import Car, Licence, Owner, Ownership

admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(Licence)
admin.site.register(Ownership)
