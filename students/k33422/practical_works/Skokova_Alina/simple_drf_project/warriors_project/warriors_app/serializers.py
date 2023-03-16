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

class ProfessionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profession
		fields = "__all__"
                
class WarriorAndProfessionSerializer(serializers.ModelSerializer):

    profession = ProfessionSerializer()

    race = serializers.CharField(source="get_race_display", read_only=True)

    class Meta:
        model = Warrior
        fields = "__all__"

class WarriorAndSkillSerializer(serializers.ModelSerializer):

    skill = SkillSerializer(many=True)

    race = serializers.CharField(source="get_race_display", read_only=True)

    class Meta:
        model = Warrior
        fields = "__all__"


class WarriorGetSerializer(serializers.ModelSerializer):

    profession = ProfessionSerializer(read_only=True)
    skill = SkillSerializer(many=True, read_only=True)

    race = serializers.CharField(source="get_race_display", read_only=True)

    class Meta:
        model = Warrior
        fields = "__all__"