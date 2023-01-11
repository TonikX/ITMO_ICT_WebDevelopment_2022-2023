from rest_framework import serializers

from .models import *


class ProfessionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profession
		fields = "__all__"


class ProfessionCreateSerializer(serializers.Serializer):
	title = serializers.CharField(max_length=120)
	description = serializers.CharField()

	def create(self, validated_data):
		profession = Profession(**validated_data)
		profession.save()
		return profession


class SkillSerializer(serializers.ModelSerializer):
	class Meta:
		model = Skill
		fields = "__all__"


class SkillCreateSerializer(serializers.Serializer):
	title = serializers.CharField(max_length=120)

	def create(self, validated_data):
		skill = Skill(**validated_data)
		skill.save()
		return skill


class SkillOfWarriorSerializer(serializers.ModelSerializer):
	class Meta:
		model = SkillOfWarrior
		fields = ["level"]


class SkillWithLevelSerializer(serializers.ModelSerializer):
	skill_of_warrior = SkillOfWarriorSerializer(many=True)

	class Meta:
		model = Skill
		fields = ["title", "skill_of_warrior"]


class WarriorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Warrior
		fields = "__all__"


class WarriorProfessionSerializer(serializers.ModelSerializer):
	profession = ProfessionSerializer()

	class Meta:
		model = Warrior
		fields = ["id", "race", "name", "level", "profession"]


class WarriorSkillSerializer(serializers.ModelSerializer):
	skill = SkillWithLevelSerializer(many=True)

	class Meta:
		model = Warrior
		fields = ["id", "race", "name", "level", "skill"]


class WarriorFullSerializer(serializers.ModelSerializer):
	profession = ProfessionSerializer()
	skill = SkillWithLevelSerializer(many=True)
	race = serializers.CharField(source="get_race_display", read_only=True)

	class Meta:
		model = Warrior
		fields = "__all__"


class WarriorEditSerializer(serializers.ModelSerializer):
	class Meta:
		model = Warrior
		fields = ["race",
		          "name",
		          "level"]
