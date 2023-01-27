from django.contrib import admin

# Register your models here.
from .models import Warrior, Profession, SkillOfWarrior, Skill

admin.site.register(Warrior)
admin.site.register(Profession)
admin.site.register(SkillOfWarrior)
admin.site.register(Skill)