from django.contrib import admin
from .models import Tour, Reservation, Review

admin.site.register(Tour)
admin.site.register(Reservation)


# Администратор может смотреть и удалять комментарии, но не может редактировать или создавать их
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False