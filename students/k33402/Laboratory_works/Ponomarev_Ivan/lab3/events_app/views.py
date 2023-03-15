from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *


# Create your views here.

class UserUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = MyUserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = MyUserSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = MyUserSerializer


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = MyUserSerializer


class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = MyUserSerializer


class CategoryUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDestroyAPIView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class LocationUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationCreateAPIView(generics.CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationListAPIView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDestroyAPIView(generics.DestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class EventUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventCreateAPIView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventListAPIView(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.all()
        parameters = self.request.query_params

        category = parameters.get('category', None)
        city = parameters.get('city', None)

        if category:
            queryset = queryset.filter(category=category)

        if city:
            queryset = queryset.filter(place__city=city)

        return queryset


class EventDestroyAPIView(generics.DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class UserEventEnrollmentUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = UserEventEnrollment.objects.all()
    serializer_class = UserEventEnrollmentSerializer


class UserEventEnrollmentCreateAPIView(generics.CreateAPIView):
    queryset = UserEventEnrollment.objects.all()
    serializer_class = UserEventEnrollmentSerializer


class UserEventEnrollmentListAPIView(generics.ListAPIView):
    queryset = UserEventEnrollment.objects.all()
    serializer_class = UserEventEnrollmentSerializer

    def get_queryset(self):
        queryset = UserEventEnrollment.objects.all()

        parameters = self.request.query_params

        user = parameters.get('user_id')

        if user:
            queryset = queryset.filter(user_id=user)

        return queryset


class UserEventEnrollmentDestroyAPIView(generics.DestroyAPIView):
    queryset = UserEventEnrollment.objects.all()
    serializer_class = UserEventEnrollmentSerializer


class UserEventEnrollmentRetrieveAPIView(generics.RetrieveAPIView):
    queryset =UserEventEnrollment.objects.all()
    serializer_class = UserEventEnrollmentSerializer



