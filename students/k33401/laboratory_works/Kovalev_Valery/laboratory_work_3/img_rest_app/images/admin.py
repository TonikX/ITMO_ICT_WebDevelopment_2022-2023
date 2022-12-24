from django.contrib import admin
from .models import *

admin.site.register(Photo)
admin.site.register(Conversion)
admin.site.register(Keyword)
admin.site.register(Color)
admin.site.register(Collection)
admin.site.register(LikePhoto)
admin.site.register(CollectionPhoto)
