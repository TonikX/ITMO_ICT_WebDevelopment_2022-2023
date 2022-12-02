from rest_framework import serializers
from .models import *


class WarriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = "__all__"


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class WarriorProfessionSerializer(serializers.ModelSerializer):
    profession = ProfessionSerializer()

    class Meta:
        model = Warrior
        fields = "__all__"


class WarriorSkillSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(many=True)

    class Meta:
        model = Warrior
        fields = "__all__"


class WarriorRetrieveSerializer(serializers.ModelSerializer):
    profession = ProfessionSerializer()
    skill = SkillSerializer(many=True)

    class Meta:
        model = Warrior
        fields = "__all__"
