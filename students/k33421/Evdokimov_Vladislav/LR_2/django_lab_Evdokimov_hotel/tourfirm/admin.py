from django.contrib import admin
from .models import User, Tour, Feedback, Reservation

admin.site.register(User)
admin.site.register(Tour)
admin.site.register(Feedback)
admin.site.register(Reservation)
