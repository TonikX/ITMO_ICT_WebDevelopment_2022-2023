from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics


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

        return Response({"Success": "Profession '{}' created succesfully.".format(profession_saved.title)})


class ProfessionAPIView(APIView):
    def get(self, request):
        professions = Profession.objects.all()
        serializer = ProfessionSerializer(professions, many=True)
        return Response({"Profession": serializer.data})


class SkillAPIView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response({"Skill": serializer.data})


class SkillCreateView(APIView):
    def post(self, request):
        skill = request.data.get("skill")
        serializer = SkillSerializer(data=skill)

        if serializer.is_valid(raise_exception=True):
            skill_saved = serializer.save()

        return Response({"Success": "Skill '{}' created succesfully.".format(skill_saved.title)})


class WarriorListAPIView(generics.ListAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class WarriorCreateAPIView(generics.CreateAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class ProfessionCreateAPIView(generics.CreateAPIView):
    serializer_class = ProfessionSerializer
    queryset = Profession.objects.all()


class WarriorProfessionAPIView(generics.ListAPIView):
    serializer_class = WarriorProfessionSerializer
    queryset = Warrior.objects.all()


class WarriorSkillAPIView(generics.ListAPIView):
    serializer_class = WarriorSkillSerializer
    queryset = Warrior.objects.all()


class WarriorRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = WarriorRetrieveSerializer
    queryset = Warrior.objects.all()


class WarriorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()

# {
# "profession":
# {
# "title": "New Profession",
# "description": "New Profession"
# }
# }