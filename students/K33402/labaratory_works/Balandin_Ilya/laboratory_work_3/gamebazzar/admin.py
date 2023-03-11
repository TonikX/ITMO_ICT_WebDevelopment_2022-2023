from django.contrib import admin

from .models import *

admin.site.register(Genre)
admin.site.register(Platform)
admin.site.register(Game)
admin.site.register(Product)
admin.site.register(Sell)