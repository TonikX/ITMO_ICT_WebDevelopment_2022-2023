from django.contrib import admin

# Register your models here.
from apps.groups.models import Group

admin.site.register(Group)
