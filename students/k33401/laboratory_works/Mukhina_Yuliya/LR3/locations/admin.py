from django.contrib import admin
from .models import Country, City, UserChoice


admin.site.register(Country)
admin.site.register(City)
admin.site.register(UserChoice)
