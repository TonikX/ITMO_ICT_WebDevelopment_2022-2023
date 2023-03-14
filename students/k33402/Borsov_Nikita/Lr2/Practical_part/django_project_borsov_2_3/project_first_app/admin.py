from django.contrib import admin
from project_first_app.models import Owner, Property, Car, DrivingLicence


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'birthdate', 'passport_num', 'addres', 'nationality')


class PropertysAdmin(admin.ModelAdmin):
    list_display = ('car_owner_id', 'owner_id', 'car_id', 'start_date', 'end_date',)


class CarAdmin(admin.ModelAdmin):
    list_display = ('car_id', 'state_number', 'car_brand', 'car_model', 'car_color')




admin.site.register(Owner, OwnerAdmin)
admin.site.register(Property, PropertysAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(DrivingLicence)



