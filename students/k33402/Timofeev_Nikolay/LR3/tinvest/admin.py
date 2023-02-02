from django.contrib import admin
from . import models

# Register your models here.
# admin.autodiscover()

admin.site.register(models.User)
admin.site.register(models.MarketEntry)
admin.site.register(models.MarketOffer)
admin.site.register(models.MarketRequestDeal)
admin.site.register(models.UserBalance)
