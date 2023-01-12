from rest_framework import serializers
from .models import Warrior, Profession, Skill


class ProfessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profession
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = "__all__"


class WarriorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Warrior
        fields = "__all__"


class WarriorProfessionSerializer(WarriorSerializer):
    profession = ProfessionSerializer(read_only=True)


class WarriorSkillsSerializer(WarriorSerializer):
    skill = SkillSerializer(many=True)


class WarriorAllInfoSerializer(WarriorSerializer):
    profession = ProfessionSerializer(read_only=True)
    skill = SkillSerializer(many=True)
