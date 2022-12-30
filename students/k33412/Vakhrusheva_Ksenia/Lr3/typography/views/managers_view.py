from django.urls import path
from rest_framework import generics

from typography.models import Manager
from typography.serializers import PublicManagerSerializer, PrivateManagerSerializer


class ManagersApiView(generics.ListAPIView):
	queryset = Manager.objects.all()
	serializer_class = PublicManagerSerializer


class GetManagerApiView(generics.RetrieveAPIView):
	queryset = Manager.objects.all()
	serializer_class = PrivateManagerSerializer


urlpatterns = [
	path("managers/", ManagersApiView.as_view()),
	path("manager/<int:pk>", GetManagerApiView.as_view()),
]
