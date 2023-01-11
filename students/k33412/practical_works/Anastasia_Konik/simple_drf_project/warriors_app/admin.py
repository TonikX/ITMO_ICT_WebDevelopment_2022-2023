from django.contrib import admin
from .models import Warrior, Skill, Profession, SkillOfWarrior

admin.site.register([Warrior, Skill, Profession, SkillOfWarrior])