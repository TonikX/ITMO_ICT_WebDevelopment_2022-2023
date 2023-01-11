from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.views import APIView

from warriors_app.serializers import *


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


class WarriorWithProfessionView(APIView):
	def get(self, request):
		warriors = Warrior.objects.all()
		serializer = WarriorWithProfessionSerializer(warriors, many=True)
		return Response({"WarriorsWithProfession": serializer.data})


class WarriorWithSkillView(ListAPIView):
	serializer_class = WarriorWithSkillSerializer
	queryset = Warrior.objects.all()


class FullWarriorAPIView(RetrieveAPIView):
	serializer_class = FullWarriorSerializer
	queryset = Warrior.objects.all()


class DeleteWarriorView(DestroyAPIView):
	serializer_class = FullWarriorSerializer
	queryset = Warrior.objects.all()


class EditWarriorView(UpdateAPIView):
	serializer_class = EditWarriorSerializer
	queryset = Warrior.objects.all()
