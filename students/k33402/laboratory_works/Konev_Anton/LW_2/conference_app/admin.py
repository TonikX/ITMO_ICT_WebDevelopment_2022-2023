from django.contrib import admin

from conference_app.models import *

admin.site.register(Conference)
admin.site.register(ConfRegistration)
admin.site.register(ConfComment)
