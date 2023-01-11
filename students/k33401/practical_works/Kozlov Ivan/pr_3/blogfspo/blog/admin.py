from django.contrib import admin

from .models import Driver_doc, Ownership, Transport, Transport_owner

admin.site.register(Transport_owner)
admin.site.register(Transport)
admin.site.register(Ownership)
admin.site.register(Driver_doc)
