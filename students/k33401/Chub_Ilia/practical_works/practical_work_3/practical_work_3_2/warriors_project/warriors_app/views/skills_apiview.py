from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Skill
from ..serializers import SkillsSerializer


class SkillsAPIView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillsSerializer(skills, many=True)
        return Response({"Skills": serializer.data})
