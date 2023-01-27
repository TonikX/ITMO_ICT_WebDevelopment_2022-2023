from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import RoomSerializer, StaffSerializer, GuestSerializer, CleaningSerializer, CheckinSerializer


class RoomAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class StaffAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()


class GuestAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = GuestSerializer
    queryset = Guest.objects.all()


class CleaningAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CleaningSerializer
    queryset = Cleaning.objects.all()


class CheckinAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CheckinSerializer
    queryset = Cleaning.objects.all()