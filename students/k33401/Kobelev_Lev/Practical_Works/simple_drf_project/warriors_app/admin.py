from django.contrib import admin
from .models import Warrior, Skill, Job, SkillOfWarrior

admin.site.register([Warrior, Skill, Job, SkillOfWarrior])
