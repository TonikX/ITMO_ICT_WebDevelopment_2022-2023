from django.apps import apps
from django.contrib import admin

myapp = apps.get_app_config('library_app')
admin.site.register(myapp.get_models())
