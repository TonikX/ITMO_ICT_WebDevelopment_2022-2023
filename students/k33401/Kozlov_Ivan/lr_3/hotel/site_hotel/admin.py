from django.contrib import admin

from .models import TypeRoom, Room, PriceConstructor, Workers, Client, Book

admin.site.register(TypeRoom)
admin.site.register(Room)
admin.site.register(PriceConstructor)
admin.site.register(Workers)
admin.site.register(Client)
admin.site.register(Book)
