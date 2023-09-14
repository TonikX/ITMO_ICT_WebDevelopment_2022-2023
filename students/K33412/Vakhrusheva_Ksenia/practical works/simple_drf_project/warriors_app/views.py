from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from warriors_app.models import Warrior, Skill
from warriors_app.serializers import WarriorSerializer, SkillSerializer, ProfessionCreateSerializer, \
	SkillCreateSerializer, WarriorProfessionSerializer, WarriorSkillSerializer, WarriorFullSerializer, \
	WarriorEditSerializer


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


class WarriorProfessionView(generics.ListAPIView):
	serializer_class = WarriorProfessionSerializer
	queryset = Warrior.objects.all()


class WarriorSkillView(generics.ListAPIView):
	serializer_class = WarriorSkillSerializer
	queryset = Warrior.objects.all()


class SingleWarriorView(generics.RetrieveAPIView):
	serializer_class = WarriorFullSerializer
	queryset = Warrior.objects.all()


class DeleteWarriorView(generics.DestroyAPIView):
	queryset = Warrior.objects.all()


class UpdateWarriorView(generics.UpdateAPIView):
	serializer_class = WarriorEditSerializer
	queryset = Warrior.objects.all()
