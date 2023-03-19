from .professions_serializer import ProfessionsSerializer
from rest_framework.serializers import ModelSerializer
from ..models import Warrior


class WarriorsWithProfessionsSerializer(ModelSerializer):
    profession = ProfessionsSerializer()

    class Meta:
        model = Warrior
        fields = "__all__"
