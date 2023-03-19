from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import SkillsCreateSerializer


class SkillsCreateView(APIView):
    def post(self, request):
        skill = request.data.get("skill")
        serializer = SkillsCreateSerializer(data=skill)

        if serializer.is_valid(raise_exception=True):
           skill_saved = serializer.save()

        return Response({"Success": "Skill'{}' created succesfully.".format(skill_saved.title)})
