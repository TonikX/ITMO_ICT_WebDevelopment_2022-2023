from django.contrib import admin
from .models import *

admin.site.register(Book)
admin.site.register(BookRoom)
admin.site.register(Reader)
admin.site.register(ReaderRoom)
admin.site.register(ReaderBook)
admin.site.register(Room)
admin.site.register(User)
admin.site.register(Instance)