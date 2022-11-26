from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from backend.app.models import Exhibition
from backend.api.app.serializers import ExhibitionSerializer


class AllExhibition(APIView):
    """Вывод всех выставок"""
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        exhibition = Exhibition.objects.all()
        ser = ExhibitionSerializer(exhibition, many=True)
        return Response(ser.data)


