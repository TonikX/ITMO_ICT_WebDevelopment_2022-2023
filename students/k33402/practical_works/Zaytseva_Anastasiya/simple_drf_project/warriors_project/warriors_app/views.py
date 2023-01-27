from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Warrior, Skill
from .serializers import WarriorSerializer, ProfessionCreateSerializer, SkillSerializer, WarriorProfessionSerializer, \
    WarriorSkillSerializer


class WarriorsAPIView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorSerializer(warriors, many=True)
        return Response({"Warriors": serializer.data})


class ProfessionCreateView(APIView):
    def post(self, request):
        profession = request.data.get("profession")
        serializer = ProfessionCreateSerializer(data=profession)

        if serializer.is_valid(raise_exception=True):
            profession_saved = serializer.save()

        return Response({"Success": "Profession '{}' created succesfully.".format(profession_saved.title)})


class SkillAPIView(APIView):
    def get(self, request):
        warriors = Skill.objects.all()
        serializer = SkillSerializer(warriors, many=True)
        return Response({"Skills": serializer.data})


class SkillCreateView(APIView):
    def post(self, request):
        skill = request.data.get("skill")
        serializer = SkillSerializer(data=skill)

        if serializer.is_valid(raise_exception=True):
            skill_saved = serializer.save()

        return Response({"Success": "Skill '{}' created succesfully.".format(skill_saved.title)})


class WarriorProfessionAPIView(generics.ListAPIView):
    serializer_class = WarriorProfessionSerializer
    queryset = Warrior.objects.all()


class WarriorSkillAPIView(generics.ListAPIView):
    serializer_class = WarriorSkillSerializer
    queryset = Warrior.objects.all()


class WarriorAPIView(generics.RetrieveAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class DeleteWarriorAPIView(generics.DestroyAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class EditWarriorAPIView(generics.UpdateAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()
