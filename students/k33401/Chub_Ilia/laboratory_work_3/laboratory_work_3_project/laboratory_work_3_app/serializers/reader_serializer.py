from rest_framework import serializers
from ..models import ReaderModel


class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReaderModel
        fields = "__all__"
