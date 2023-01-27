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


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class SkillRelatedSerializer(serializers.ModelSerializer):
    warrior_skills = WarriorSerializer(many=True)

    class Meta:
        model = Skill
        fields = ["title", "warrior_skills"]


class WarriorFullInfoSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(many=True)
    profession = ProfessionSerializer()

    class Meta:
        model = Warrior
        fields = "__all__"


'''
class WarriorDepthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warrior
        fields = "__all__"

        # добавляем глубину
        depth = 1
'''


class WarriorNestedSerializer(serializers.ModelSerializer):
    # делаем наследование
    profession = ProfessionCreateSerializer()
    skill = SkillSerializer(many=True)
    # уточняем поле
    race = serializers.CharField(source="get_race_display", read_only=True)

    class Meta:
        model = Warrior
        fields = "__all__"
