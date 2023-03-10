from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Warrior, Profession, Skill, SkillOfWarrior
from .serializers import WarriorSerializer, ProfessionCreateSerializer, SkillSerializer, SkillCreateSerializer, WarriorAndProfessionSerializer, WarriorAndSkillSerializer, WarriorDetailsSerializer


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

        return Response({"Success": "Profession '{}' created succesfully.".format(profession_saved.title)})


class SkillAPIView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response({"Skills": serializer.data})


class SkillCreateView(APIView):

    def post(self, request):
        skill = request.data.get("skill")
        serializer = SkillCreateSerializer(data=skill)

        if serializer.is_valid(raise_exception=True):
            skill_saved = serializer.save()

        return Response({"Success": "Skill '{}' created succesfully.".format(skill_saved.title)})


class WarriorAndProfessionAPIView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorAndProfessionSerializer(warriors, many=True)
        return Response({"Warriors": serializer.data})


class WarriorAndSkillAPIView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorAndSkillSerializer(warriors, many=True)
        return Response({"Warriors": serializer.data})


class WarriorDetailsAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        warrior = Warrior.objects.get(pk=pk)
        serializer = WarriorDetailsSerializer(warrior)
        return Response({"warrior": serializer.data})

    def delete(self, request, pk, *args, **kwargs):
        warrior = Warrior.objects.get(pk=pk)
        warrior.delete()
        return Response({"Success": "Success"})

    def patch(self, request, pk, *args, **kwargs):
        warrior = Warrior.objects.get(pk=pk)

        warrior_data = request.data.get("warrior")
        serializer = WarriorDetailsSerializer(
            warrior, data=warrior_data, partial=True)

        if serializer.is_valid(raise_exception=True):
            warrior_saved = serializer.save()

        return Response({"Success": "Warrior '{}' updated succesfully.".format(warrior_saved)})
