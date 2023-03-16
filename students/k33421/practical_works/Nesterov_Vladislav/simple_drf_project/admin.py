from django.contrib import admin
from .models import Owner, Ownage, Auto, License

admin.site.register(Auto)
admin.site.register(Owner)
admin.site.register(Ownage)
admin.site.register(License)
