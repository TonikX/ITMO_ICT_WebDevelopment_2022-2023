from rest_framework import serializers
from .models import *


class WarriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = "__all__"


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ["title", "description"]


class JobCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()

    def create(self, validated_data):
        job = Job(**validated_data)
        job.save()
        return Job(**validated_data)


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class SkillCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)

    def create(self, validated_data):
        skill = Skill(**validated_data)
        skill.save()
        return Skill(**validated_data)


class WarriorJobSerializer(WarriorSerializer):
    job = JobSerializer()


class WarriorSkillsSerializer(WarriorSerializer):
    skill = SkillSerializer(many=True)


class AllWarriorsInformationSerializer(WarriorJobSerializer, WarriorSkillsSerializer):
    pass
