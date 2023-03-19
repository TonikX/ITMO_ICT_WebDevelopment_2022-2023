from rest_framework.serializers import ModelSerializer
from ..models import Skill


class SkillsSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"
