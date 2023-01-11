from django.contrib import admin
from .models import Theme, Conference, Place, PlannedConference, RegisteredConference, Comment

# Register your models here.
admin.site.register(Theme)
admin.site.register(Conference)
admin.site.register(Place)
admin.site.register(PlannedConference)
admin.site.register(RegisteredConference)
admin.site.register(Comment)
