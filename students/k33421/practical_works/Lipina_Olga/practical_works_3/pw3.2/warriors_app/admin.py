from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Warrior)
admin.site.register(Profession)
admin.site.register(Skill)
admin.site.register(SkillOfWarrior)