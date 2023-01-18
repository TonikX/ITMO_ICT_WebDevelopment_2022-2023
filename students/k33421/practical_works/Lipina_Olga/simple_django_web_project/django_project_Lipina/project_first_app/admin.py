from django.contrib import admin
from .models import Owner, Auto, License, Owning

admin.site.register(Owner)
admin.site.register(Auto)
admin.site.register(Owning)
admin.site.register(License)

# Register your models here.
