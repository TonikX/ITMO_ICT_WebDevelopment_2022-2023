from rest_framework.generics import ListAPIView
from ..models import Warrior
from ..serializers import WarriorsWithSkillsSerializer


class WarriorsWithSkillsView(ListAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorsWithSkillsSerializer
