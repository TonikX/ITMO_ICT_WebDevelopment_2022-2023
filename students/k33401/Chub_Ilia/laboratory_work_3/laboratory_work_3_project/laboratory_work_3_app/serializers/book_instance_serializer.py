from rest_framework import serializers
from ..models import BookInstanceModel


class BookInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInstanceModel
        fields = "__all__"
