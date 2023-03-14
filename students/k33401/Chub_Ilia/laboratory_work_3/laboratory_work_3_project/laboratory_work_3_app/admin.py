from django.contrib import admin
from .models import *

admin.site.register(BookInstanceModel)
admin.site.register(BookModel)
admin.site.register(ReaderBookModel)
admin.site.register(ReaderModel)
admin.site.register(ReaderRoomModel)
admin.site.register(RoomModel)
admin.site.register(UserModel)
admin.site.register(UserReaderModel)
