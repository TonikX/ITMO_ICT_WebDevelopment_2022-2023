from rest_framework import serializers
from .models import *


class WarriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = "__all__"


class ProfessionCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()

    def create(self, validated_data):
        profession = Profession(**validated_data)
        profession.save()
        return Profession(**validated_data)


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class SkillCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()

    def create(self, validated_data):
        skill = Skill(**validated_data)
        skill.save()
        return Skill(**validated_data)


class WarriorsProfessionSerializer(WarriorSerializer):
    profession = ProfessionCreateSerializer(read_only=True)


class WarriorsSkillsSerializer(WarriorSerializer):
    skill = SkillCreateSerializer(many=True, read_only=True)


class AllInformationSerializer(WarriorsProfessionSerializer, WarriorsSkillsSerializer):
    pass
