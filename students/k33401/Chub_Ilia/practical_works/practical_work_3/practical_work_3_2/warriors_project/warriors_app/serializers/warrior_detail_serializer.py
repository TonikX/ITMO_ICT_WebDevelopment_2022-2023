from rest_framework import serializers
from ..models import Warrior


class WarriorDetailsSerializer(serializers.ModelSerializer):
    # race = serializers.CharField(source="get_race_display", read_only=True)

    class Meta:
        model = Warrior
        fields = "__all__"
        # depth = 1
