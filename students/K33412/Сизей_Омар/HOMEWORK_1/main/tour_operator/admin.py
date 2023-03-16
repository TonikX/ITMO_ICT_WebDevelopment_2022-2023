from django.contrib import admin
from .models import Tourist, Tour, Reservation, Comment, Agency, Country

class Tourist_Admin(admin.ModelAdmin):
    pass

class Tour_Admin(admin.ModelAdmin):
    pass

class Reservation_Admin(admin.ModelAdmin):
    pass

class Comment_Admin(admin.ModelAdmin):
    pass

class Agency_Admin(admin.ModelAdmin):
    pass

class Country_Admin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Tourist, Tourist_Admin)
admin.site.register(Tour, Tour_Admin)
admin.site.register(Reservation, Reservation_Admin)
admin.site.register(Comment, Comment_Admin)
admin.site.register(Agency, Agency_Admin)
admin.site.register(Country, Country_Admin)















