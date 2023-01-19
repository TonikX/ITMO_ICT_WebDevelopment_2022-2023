from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *


class WarriorAPIView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorSerializer(warriors, many=True)
        return Response({"Warriors": serializer.data})


class ProfessionCreateView(APIView):
    def post(self, request):
        profession = request.data.get("profession")
        serializer = ProfessionSerializer(data=profession)

        if serializer.is_valid(raise_exception=True):
            profession_saved = serializer.save()

        return Response({"Success": "Profession '{}' created successfully.".format(profession_saved.title)})


class SkillAPIView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response({"Skills": serializer.data})


class SkillCreateView(APIView):
    def post(self, request):
        skill = request.data.get("skill")
        serializer = SkillSerializer(data=skill)

        if serializer.is_valid(raise_exception=True):
            skill_saved = serializer.save()

        return Response({"Success": "Skill '{}' created successfully.".format(skill_saved.title)})


class SkillOfWarriorCreateView(generics.CreateAPIView):
    serializer_class = SkillOfWarriorSerializer
    queryset = SkillOfWarrior.objects.all()


class WarriorProfessionView(generics.ListAPIView):
    """
    Вывод полной информации о всех воинах и их профессиях (в одном запросе)
    """
    serializer_class = WarriorProfessionSerializer
    queryset = Warrior.objects.all()


class WarriorSkillView(generics.ListAPIView):
    """
    Вывод полной информации о всех войнах и их скиллах (в одном запросе)
    """
    serializer_class = WarriorSkillSerializer
    queryset = Warrior.objects.all()


class WarriorInfoAPIView(generics.RetrieveAPIView):
    """
    Вывод полной информации о войне (по id), его профессиях и скилах
    """
    serializer_class = WarriorInfoSerializer
    queryset = Warrior.objects.all()


class WarriorDeleteView(generics.DestroyAPIView):
    """
    Удаление война по id
    """
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class WarriorEditView(generics.UpdateAPIView):
    """
    Редактирование информации о войне
    """
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()
