from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny

from .models import Hotel, RoomType, Room
from .serializers import HotelSerializer, RoomTypeSerializer, RoomSerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.permission_classes = [AllowAny, ]
        elif self.action in ('retrieve', 'create', 'update', 'destroy'):
            self.permission_classes = [IsAdminUser, ]
        return [permission() for permission in self.permission_classes]


class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.permission_classes = [AllowAny, ]
        elif self.action in ('retrieve', 'create', 'update', 'destroy'):
            self.permission_classes = [IsAdminUser, ]
        return [permission() for permission in self.permission_classes]


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.permission_classes = [AllowAny, ]
        elif self.action in ('retrieve', 'create', 'update', 'destroy'):
            self.permission_classes = [IsAdminUser, ]
        return [permission() for permission in self.permission_classes]
