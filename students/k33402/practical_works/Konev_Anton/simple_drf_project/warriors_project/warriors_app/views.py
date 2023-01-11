from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, DestroyAPIView, UpdateAPIView
from .models import Warrior, Skill
from .serializers import WarriorSerializer, ProfessionCreateSerializer, SkillsSerializer,\
    SkillCreateSerializer, WarriorsProfessionSerializer, WarriorsSkillsSerializer, AllInformationSerializer


# Create your views here.
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


class SkillsApiView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillsSerializer(skills, many=True)
        return Response({"Skills": serializer.data})


class SkillsCreateView(APIView):
    def post(self, request):
        skill = request.data.get("skill")
        serializer = SkillCreateSerializer(data=skill)

        if serializer.is_valid(raise_exception=True):
            skill_saved = serializer.save()

        return Response({"Success": "Skill'{}' created successfully.".format(skill_saved.title)})


class WarriorsProfessionView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorsProfessionSerializer(warriors, many=True)
        return Response({"Warriors": serializer.data})


class WarriorsSkillsView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorsSkillsSerializer(warriors, many=True)
        return Response({"Warriors": serializer.data})


class AllInformationView(RetrieveAPIView):
    queryset = Warrior.objects.all()
    serializer_class = AllInformationSerializer


class DeleteWarrior(DestroyAPIView):
    queryset = Warrior.objects.all()


class UpdateWarrior(UpdateAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer
