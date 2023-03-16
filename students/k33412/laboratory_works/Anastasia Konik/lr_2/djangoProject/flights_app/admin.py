from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Flight)
admin.site.register(Ticket)
admin.site.register(Feedback)
