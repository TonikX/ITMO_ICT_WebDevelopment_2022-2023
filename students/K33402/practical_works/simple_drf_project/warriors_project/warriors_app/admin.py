from django.contrib import admin

from .models import Profession, Skill, SkillOfWarrior, Warrior

admin.site.register(Warrior)
admin.site.register(Profession)
admin.site.register(Skill)
admin.site.register(SkillOfWarrior)
