from django.contrib import admin

# Register your models here.
from .models import Airline, Passenger, Review, Air_travel

admin.site.register(Airline)
admin.site.register(Passenger)
admin.site.register(Review)
admin.site.register(Air_travel)
