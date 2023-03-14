from rest_framework import serializers
from ..models import ReaderRoomModel


class ReaderRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReaderRoomModel
        fields = "__all__"
