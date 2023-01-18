from rest_framework import serializers
from .models import *


class WarriorSerializer(serializers.ModelSerializer):

  class Meta:
     model = Warrior
     fields = "__all__"

class  ProfessionSerializer(serializers.ModelSerializer):

  class Meta:
     model = Profession
     fields = "__all__"

class SkillSerializer(serializers.ModelSerializer):

  class Meta:
     model = Skill
     fields = "__all__"


class WarriorProfessionSerializer(WarriorSerializer):
    profession = ProfessionSerializer(read_only=True)

class WarriorSkillsSerializer(WarriorSerializer):
    skill = SkillSerializer(many=True, read_only=True)

class AllWarriorsInformationSerializer(WarriorProfessionSerializer, WarriorSkillsSerializer):
    pass

