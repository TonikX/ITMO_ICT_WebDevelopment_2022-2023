from rest_framework import serializers
from ..models import Warrior


class WarriorsWithSkillsSerializer(serializers.ModelSerializer):
    skill = serializers.StringRelatedField(read_only=True, many=True)

    class Meta:
        model = Warrior
        fields = "__all__"
