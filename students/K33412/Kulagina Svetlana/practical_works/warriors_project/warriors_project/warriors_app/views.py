from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView, Response
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
        serializer = ProfessionCreateSerializer(data=profession)

        if serializer.is_valid(raise_exception=True):
            profession_saved = serializer.save()

        return Response({"Success": "Profession '{}' created succesfully.".format(profession_saved.title)})


class ProfessionAPIView(APIView):

    def get(self, request):
        professions = Profession.objects.all()
        serializer = ProfessionSerializer(professions, many=True)
        return Response({"Professions": serializer.data})


class WarriorListAPIView(generics.ListAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class ProfessionCreateAPIView(generics.CreateAPIView):
    serializer_class = ProfessionCreateSerializer
    queryset = Profession.objects.all()


class WarriorsProfessionsListAPIView(generics.ListAPIView):
    serializer_class = WarriorsProfessionsSerializer
    queryset = Warrior.objects.all()


class SkillAPIView(generics.ListAPIView):
    serializer_class = SkillRelatedSerializer
    queryset = Skill.objects.all()


class WarriorRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WarriorRelatedSerializer
    queryset = Warrior.objects.all()