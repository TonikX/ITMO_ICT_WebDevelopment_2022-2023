from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import Transport_owner_form
from .models import Driver_doc, Ownership, Transport, Transport_owner


@admin.register(Transport_owner)
class Transport_owner_reg_in_admin(UserAdmin):
    model = Transport_owner
    add_form = Transport_owner_form


admin.site.register(Transport)
admin.site.register(Ownership)
admin.site.register(Driver_doc)
