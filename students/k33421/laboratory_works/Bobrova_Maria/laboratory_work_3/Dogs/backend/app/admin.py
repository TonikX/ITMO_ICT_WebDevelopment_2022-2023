from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from backend.app.models import Show, Ring, Expert, Participant, Participation, Club


class PostAdmin(MPTTModelAdmin):
    """Сообщения"""
    list_display = ("id", "user", "text", "parent", "like", "date")
    mptt_level_indent = 20

admin.site.register(Show)
admin.site.register(Ring)
admin.site.register(Expert)
admin.site.register(Participant)
admin.site.register(Participation)
admin.site.register(Club)