from django.contrib import admin

from users.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'grade',
        'is_staff',
    )
    search_fields = ('first_name', 'last_name')
    list_filter = ('last_name',)
    empty_value_display = '-пусто-'


admin.site.register(User, UserAdmin)
