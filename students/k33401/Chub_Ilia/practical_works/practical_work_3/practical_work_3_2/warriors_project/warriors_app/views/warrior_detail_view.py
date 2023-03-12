from rest_framework.generics import RetrieveUpdateDestroyAPIView
from ..models import Warrior
from ..serializers import WarriorDetailsSerializer


class WarriorDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = WarriorDetailsSerializer
    queryset = Warrior.objects.all()
