from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from django.contrib.auth.models import User

from .serializers import MyUserSerializer
from .permissions import IsOwner


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = MyUserSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny, ]
        elif self.action in ('list', 'retrieve', 'update', 'destroy'):
            self.permission_classes = [IsAdminUser | IsOwner, ]
        return [permission() for permission in self.permission_classes]
