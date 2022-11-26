from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from backend.app.models import Exhibition, Competition, DogOwner, Expert, ExpertCompetition,\
    Dog, DogRegistration, Result, CompParticipation, Club, ClubParticipation, Dismissed


class PostAdmin(MPTTModelAdmin):
    """Сообщения"""
    list_display = ("id", "user", "text", "parent", "like", "date")
    mptt_level_indent = 20

admin.site.register(Exhibition)
admin.site.register(Competition)
admin.site.register(DogOwner)
admin.site.register(Expert)
admin.site.register(ExpertCompetition)
admin.site.register(Dog)
admin.site.register(DogRegistration)
admin.site.register(Result)
admin.site.register(CompParticipation)
admin.site.register(Club)
admin.site.register(ClubParticipation)
admin.site.register(Dismissed)