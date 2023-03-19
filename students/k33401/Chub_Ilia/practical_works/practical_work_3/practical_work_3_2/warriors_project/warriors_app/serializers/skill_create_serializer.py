from rest_framework.serializers import ModelSerializer
from ..models import Skill


class SkillsCreateSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"
