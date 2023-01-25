from django.contrib import admin
from .models import *

admin.site.register(Book)
admin.site.register(Hall)
admin.site.register(Reader)
admin.site.register(BookInHall)
admin.site.register(ReaderBook)
admin.site.register(Copy)
#admin.site.register(Report)