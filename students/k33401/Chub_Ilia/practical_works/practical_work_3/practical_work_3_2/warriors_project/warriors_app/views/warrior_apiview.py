from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Warrior
from ..serializers import WarriorSerializer


class WarriorAPIView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorSerializer(warriors, many=True)
        
        return Response({"Warriors": serializer.data})
