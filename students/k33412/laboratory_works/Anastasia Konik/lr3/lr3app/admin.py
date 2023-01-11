from django.contrib import admin
from .models import User, UserEnrolledEvent, Event, Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Event)
admin.site.register(UserEnrolledEvent)
admin.site.register(Comment)
