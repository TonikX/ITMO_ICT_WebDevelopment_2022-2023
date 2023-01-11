from rest_framework import serializers

from warriors_app.models import *


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
		return skill


class ProfessionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profession
		fields = "__all__"


class WarriorWithProfessionSerializer(serializers.ModelSerializer):
	profession = ProfessionSerializer()

	class Meta:
		model = Warrior
		fields = "__all__"


class WarriorWithSkillSerializer(serializers.ModelSerializer):
	skill = SkillSerializer(many=True)

	class Meta:
		model = Warrior
		fields = "__all__"


class FullWarriorSerializer(serializers.ModelSerializer):
	profession = ProfessionSerializer()
	skill = SkillSerializer(many=True)
	race = serializers.CharField(source="get_race_display", read_only=True)

	class Meta:
		model = Warrior
		fields = "__all__"


class EditWarriorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Warrior
		fields = ["race", "name", "level"]
