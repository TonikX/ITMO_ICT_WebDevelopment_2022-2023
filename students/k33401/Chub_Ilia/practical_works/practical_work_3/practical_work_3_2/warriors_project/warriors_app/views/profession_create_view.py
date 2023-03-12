from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import ProfessionCreateSerializer


class ProfessionCreateView(APIView):
    def post(self, request):
        profession = request.data.get("profession")

        serializer = ProfessionCreateSerializer(data=profession)

        if serializer.is_valid(raise_exception=True):
            profession_saved = serializer.save()

        return Response({"Success": "Profession '{}' created succesfully.".format(profession_saved.title)})
