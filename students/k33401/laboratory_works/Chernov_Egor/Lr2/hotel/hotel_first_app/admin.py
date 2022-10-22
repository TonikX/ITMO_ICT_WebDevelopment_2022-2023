from django.contrib import admin
from .models import *


admin.site.register(Hotel)
admin.site.register(Guest)
admin.site.register(Employee)
admin.site.register(RoomType)
admin.site.register(Room)
admin.site.register(Registration)
admin.site.register(User)

# username: admin
# mail: admin@mail.ru
# password: 12345678
