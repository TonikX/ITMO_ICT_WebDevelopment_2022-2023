from rest_framework.generics import *
from rest_framework.views import APIView
from .serializers import *


class WarriorListAPIView(ListAPIView):
    serializer_class = AllWarriorsInformationSerializer
    queryset = Warrior.objects.all()


class WarriorAPIView(RetrieveAPIView):
    serializer_class = AllWarriorsInformationSerializer
    queryset = Warrior.objects.all()


class WarriorAPIDelete(DestroyAPIView):
    queryset = Warrior.objects.all()


class WarriorAPIUpdate(UpdateAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class SkillListAPIView(APIView):
    serializers_class = SkillSerializer
    queryset = Skill.objects.all()


class JobsListAPIView(ListAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()


class JobCreateAPIView(CreateAPIView):
    serializer_class = JobCreateSerializer
    queryset = Job.objects.all()


class SkillCreateAPIView(CreateAPIView):
    serializer_class = SkillCreateSerializer
    queryset = Skill.objects.all()
