from django.contrib import admin
from .models import Owner, Car, Owning, License
# Register your models here.
admin.site.register(Owner)
admin.site.register(Owning)
admin.site.register(Car)
admin.site.register(License)