from django.contrib import admin

from .models import User, Conference, Comment

admin.site.register(User)
admin.site.register(Conference)
admin.site.register(Comment)
