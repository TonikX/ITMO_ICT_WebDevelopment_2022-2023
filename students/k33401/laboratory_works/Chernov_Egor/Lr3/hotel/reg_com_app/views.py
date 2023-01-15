from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny

from .models import Registration, Comment
from .serializers import RegistrationSerializer, CommentSerializer
from .permisions import IsOwner


class RegistrationViewSet(viewsets.ModelViewSet):
    serializer_class = RegistrationSerializer
    permission_classes = [IsAdminUser | IsOwner, ]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Registration.objects.all()
        return Registration.objects.filter(user_reg=user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.permission_classes = [AllowAny, ]
        elif self.action in ('create', 'update', 'destroy'):
            self.permission_classes = [IsAdminUser | IsOwner, ]
        return [permission() for permission in self.permission_classes]
