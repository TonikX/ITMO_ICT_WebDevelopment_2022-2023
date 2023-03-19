from rest_framework.generics import ListAPIView
from ..models import Warrior
from ..serializers import WarriorsWithProfessionsSerializer


class WarriorsWithProfessionsView(ListAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorsWithProfessionsSerializer
