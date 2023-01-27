from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, DestroyAPIView, UpdateAPIView
from .serializers import WarriorSerializer, SkillSerializer, ProfessionSerializer, WarriorProfessionSerializer, WarriorSkillsSerializer, WarriorProfessionsSkillsSerializer
from .models import *

# Show warriors
class WarriorAPIView(APIView):
   def get(self, request):
       warriors = Warrior.objects.all()
       serializer = WarriorSerializer(warriors, many=True)
       return Response({"Warriors": serializer.data})


# Create new professions
class ProfessionCreateView(APIView):

    def post(self, request):
        profession = request.data.get("profession")
        serializer = ProfessionSerializer(data=profession)

        if serializer.is_valid(raise_exception=True):
            profession_saved = serializer.save()

        return Response({"Success": "Profession '{}' created successfully.".format(profession_saved.title)})


# Show skills
class SkillsAPIView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response({"Skills": serializer.data})


# Create new skills
class SkillCreateView(APIView):
    def post(self, request):
        skill = request.data.get("skill")
        serializer = SkillSerializer(data=skill)

        if serializer.is_valid(raise_exception=True):
            skill_saved = serializer.save()

        return Response({"Success": "Skill '{}' created successfully.".format(skill_saved.title)})


# Show full info about warriors and their professions
class WarriorProfessionView(APIView):

    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorProfessionSerializer(warriors, many=True)
        return Response({"warriors": serializer.data})


# Show full info about warriors and their skills
class WarriorsSkillsView(APIView):

    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorSkillsSerializer(warriors, many=True)
        return Response({"warriors": serializer.data})


# Show full info about warriors (by id) and their professions, skills
class WarriorInfoView(RetrieveAPIView):
    
    queryset = Warrior.objects.all()
    serializer_class = WarriorProfessionsSkillsSerializer


# Delete a warrior by id
class WarriorDeleteView(DestroyAPIView):

    queryset = Warrior.objects.all()


# Edit info about a warrior
class WarriorEditView(UpdateAPIView):
    
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": f"warrior {instance} updated successfully"})

        else:
            return Response({"message": "failed", "details": serializer.errors})