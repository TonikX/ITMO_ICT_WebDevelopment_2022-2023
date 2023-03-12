from rest_framework import serializers
from ..models import Profession


class ProfessionCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()

    def create(self, validated_data):
        profession = Profession(**validated_data)
        profession.save()

        return Profession(**validated_data)
