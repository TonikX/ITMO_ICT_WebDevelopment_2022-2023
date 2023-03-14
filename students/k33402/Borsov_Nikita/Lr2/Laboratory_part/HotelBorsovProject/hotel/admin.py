from django.contrib import admin
from hotel.models import *


class GuestAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'username', 'name', 'surname')


class RoomAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'capacity', 'prestigue', 'cost', 'facilities', 'resident')


class BookingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'guest', 'room', 'checkin_date', 'checkout_date')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'room', 'author', 'text', 'rating')


admin.site.register(Guest, GuestAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Comment, CommentAdmin)
