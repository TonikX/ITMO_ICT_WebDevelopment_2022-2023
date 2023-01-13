from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView

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

class SkillsApiView(APIView):
     def get(self, request):
       skills = Skill.objects.all()
       serializer = SkillSerializer(skills, many=True)
       return Response({"Skills": serializer.data})

class SkillsCreateView(APIView):

   def post(self, request):
       skill = request.data.get("skill")
       serializer = SkillsCreateSerializer(data=skill)

       if serializer.is_valid(raise_exception=True):
           skill_saved = serializer.save()

       return Response({"Success": "Skill'{}' created succesfully.".format(skill_saved.title)})

class WarriorProfessionView(APIView):
    """
    Вывод полной информации о всех войнах и их профессиях (в одном запросе).
    """
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorProfessionSerializer(warriors, many=True)
        return Response({"warriors": serializer.data})

class WarriorsSkillsView(APIView):
    """
    Вывод полной информации о всех войнах и их скиллах (в одном запросе)
    """
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorSkillsSerializer(warriors, many=True)
        return Response({"warriors": serializer.data})

class AllWarriorsInformation(RetrieveAPIView):
    """ Вывод полной информации о войне (по id), его профессиях и скилах. """
    queryset = Warrior.objects.all()
    serializer_class = AllWarriorsInformationSerializer

class DeleteWarrior(DestroyAPIView):
    """ Удаление война по id. """
    queryset = Warrior.objects.all()

class UpdateWarrior(UpdateAPIView):
    """ Редактирование информации о войне. """
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer
