from django.contrib import admin
from .models import Flight, Airplane, Crew, Transit, Worker, Airport, Manager
# Register your models here.


admin.site.register(Manager)
admin.site.register(Flight)
admin.site.register(Airplane)
admin.site.register(Crew)
admin.site.register(Transit)
admin.site.register(Worker)
admin.site.register(Airport)