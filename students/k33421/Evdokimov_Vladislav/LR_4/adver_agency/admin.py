from django.contrib import admin
from .models import *

admin.site.register(Client)
admin.site.register(ServicesPL)
admin.site.register(MaterialsPL)
admin.site.register(Request)
admin.site.register(ChosenServices)
admin.site.register(ChosenMaterials)
admin.site.register(WorkGroup)
admin.site.register(Staff)
admin.site.register(PaymentOrder)
admin.site.register(User)