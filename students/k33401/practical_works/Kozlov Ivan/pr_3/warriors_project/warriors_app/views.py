from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Warrior, Profession, SkillOfWarrior, Skill
from .serializers import WarriorSerializer, SkillsSerializer, \
    ProfessionCreateSerializer, SkillCreateSerializer, WarriorsWithSkillsSerializer, ProffesionForWarriorsSerializer
from rest_framework import serializers, generics, status

class WarriorAPIView(APIView):
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

        return Response({"Success": "Profession '{}' created successfully.".format(profession_saved.title)})


class SkillsAPIView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillsSerializer(skills, many=True)
        return Response({"Skills": serializer.data})


class SkillCreateView(APIView):
    def post(self, request):
        skill = request.data.get("skill")
        serializer = SkillCreateSerializer(data=skill)

        if serializer.is_valid(raise_exception=True):
            skill_saved = serializer.save()

        return Response({"Success": "Skill '{}' created successfully.".format(skill_saved.title)})


class WarriorListView(generics.ListAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorsWithSkillsSerializer

    # def get(self, request):
    #     warriors = Warrior.objects.all()
    #     serializer = WarriorsWithSkillsSerializer(warriors, many=True)
    #
    #     return Response({"Warriors": serializer.data})


class WarriorView(APIView):
    def get(self, request, pk):
        warriors = Warrior.objects.filter(pk=pk)
        serializer = WarriorsWithSkillsSerializer(warriors, many=True)
        return Response({"Warriors": serializer.data})


class DelWarriorView(APIView):
    def delete(self, request, pk):
        warriors = Warrior.objects.filter(pk=pk)
        warriors.delete()
        return Response(status=status.HTTP_200_OK)


class UpdateWarriors(generics.UpdateAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer
