from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Warrior, Skill, Profession
from .serializers import WarriorSerializer, ProfessionSerializer, SkillSerializer, WarriorProfessionSerializer, \
    WarriorSkillsSerializer, WarriorAllInfoSerializer


class WarriorAPIView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorSerializer(warriors, many=True)
        return Response({"Warriors": serializer.data})


class WarriorProfessionAPIView(generics.ListAPIView):
    """
    Вывод полной информации о всех войнах и их профессиях (в одном запросе).
    """
    serializer_class = WarriorProfessionSerializer
    queryset = Warrior.objects.all()


class WarriorSkillsAPIView(generics.ListAPIView):
    """
    Вывод полной информации о всех войнах и их скилах (в одном запросе).
    """
    serializer_class = WarriorSkillsSerializer
    queryset = Warrior.objects.all()


class WarriorFullInfoApiView(generics.RetrieveAPIView):
    """
    Вывод полной информации о войне (по id), его профессиях и скилах.
    """
    serializer_class = WarriorAllInfoSerializer
    queryset = Warrior.objects.all()


class WarriorUpdateApiView(generics.UpdateAPIView):
    """
    Редактирование информации о войне.
    """
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class WarriorDeleteApiView(generics.DestroyAPIView):
    """
    Удаление война по id.
    """
    queryset = Warrior.objects.all()


class SkillAPIView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response({"Skills": serializer.data})


class WarriorCreateAPIView(generics.CreateAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class ProfessionAPIView(generics.ListAPIView):
    serializer_class = ProfessionSerializer
    queryset = Profession.objects.all()


class ProfessionCreateView(APIView):
    def post(self, request):
        profession = request.data.get("profession")
        serializer = ProfessionSerializer(data=profession)

        if serializer.is_valid(raise_exception=True):
            profession_saved = serializer.save()

            return Response({"Success": "Profession '{}' created succesfully.".format(profession_saved.title)})


class ProfessionCreateAPIView(generics.CreateAPIView):
    serializer_class = ProfessionSerializer
    queryset = Profession.objects.all()


class SkillCreateView(APIView):
    def post(self, request):
        skill = request.data.get("skill")
        serializer = SkillSerializer(data=skill)

        if serializer.is_valid(raise_exception=True):
            skill_saved = serializer.save()

            return Response({"Success": "Skill '{}' created succesfully.".format(skill_saved.title)})
