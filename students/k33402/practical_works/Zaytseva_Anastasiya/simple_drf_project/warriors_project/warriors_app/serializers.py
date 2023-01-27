from rest_framework import serializers
from .models import *


class WarriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = "__all__"


class ProfessionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = "__all__"


class WarriorProfessionSerializer(serializers.ModelSerializer):
    profession = ProfessionCreateSerializer()

    class Meta:
        model = Warrior
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class SkillOfWarriorSerializer(serializers.ModelSerializer):
    skill = SkillSerializer()

    class Meta:
        model = SkillOfWarrior
        fields = ("level", "skill")

    def get_skill(self, sow_instance):
        return sow_instance.skill


class WarriorSkillSerializer(serializers.ModelSerializer):
    skill = serializers.SerializerMethodField()

    class Meta:
        model = Warrior
        fields = "__all__"

    def get_skill(self, warrior_instance):
        query_datas = SkillOfWarrior.objects.filter(warrior=warrior_instance)
        return [SkillOfWarriorSerializer(skil).data for skil in query_datas]
