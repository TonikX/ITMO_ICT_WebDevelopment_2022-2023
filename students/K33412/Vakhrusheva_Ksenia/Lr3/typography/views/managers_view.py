from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from typography.auth import ManagerAuthentication
from typography.models import Manager
from typography.serializers import PublicManagerSerializer, PrivateManagerSerializer


class ManagersApiView(generics.ListAPIView):
	queryset = Manager.objects.all()
	serializer_class = PublicManagerSerializer
	authentication_classes = [ManagerAuthentication]
	permission_classes = [IsAuthenticated]


class GetManagerApiView(generics.RetrieveAPIView):
	queryset = Manager.objects.all()
	serializer_class = PrivateManagerSerializer
	authentication_classes = [ManagerAuthentication]
	permission_classes = [IsAuthenticated]
