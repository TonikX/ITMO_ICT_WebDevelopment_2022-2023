from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import serializers, generics
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework.views import APIView

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


class ProfessionCreateAPIView(generics.CreateAPIView):
    serializer_class = ProfessionSerializer
    queryset = Profession.objects.all()


class WarriorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()
