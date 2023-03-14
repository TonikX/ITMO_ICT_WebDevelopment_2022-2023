from rest_framework import serializers
from ..models import UserReaderModel


class UserReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReaderModel
        fields = "__all__"
