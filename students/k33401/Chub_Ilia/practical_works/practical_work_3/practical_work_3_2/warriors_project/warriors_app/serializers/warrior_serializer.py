from rest_framework.serializers import ModelSerializer
from ..models import Warrior


class WarriorSerializer(ModelSerializer):
    class Meta:
        model = Warrior
        fields = "__all__"
