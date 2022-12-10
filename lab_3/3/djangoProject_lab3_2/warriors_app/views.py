
from rest_framework import serializers, generics
from .models import *

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

class WarriorAndSkillsSerializer(serializers.ModelSerializer):
    warriors = WarriorSerializer
    skill = SkillSerializer(many=True)

    class Meta:
        model = Warrior
        fields = "__all__"


class WarriorAndProfessionSerializer(serializers.ModelSerializer):
    warriors = WarriorSerializer
    profession = ProfessionSerializer(allow_null=True)

    class Meta:
        model = Warrior
        fields = "__all__"


class WarriorAndSkillsAPIView(generics.ListAPIView):
    serializer_class = WarriorAndSkillsSerializer
    queryset = Warrior.objects.all()


class WarriorAndProfessionAPIView(generics.ListAPIView):
    serializer_class = WarriorAndProfessionSerializer
    queryset = Warrior.objects.all()


class ProfessionCrateAPIView(generics.CreateAPIView):
    serializer_class = ProfessionSerializer
    queryset = Profession.objects.all()


class WarriorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()
