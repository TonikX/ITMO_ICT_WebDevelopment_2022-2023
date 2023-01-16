from django.shortcuts import render
from rest_framework import views, permissions
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView
from .serializers import *
from .models import *
from django.db.models import Count
from rest_framework.response import Response

class EventsList(ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.all()
        category = self.request.query_params.get('category')
        district = self.request.query_params.get('district')
        type_event = self.request.query_params.get('type_event')

        if (type_event is not None) and (type_event != ''):
            queryset = queryset.filter(type_event=type_event)
        if (category is not None) and (category != ''):
            queryset = queryset.filter(category=category)
        if (district is not None) and (district != ''):
            queryset = queryset.filter(district=district)

        return queryset

class EventRetrieve(RetrieveAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class UserList(ListAPIView):
    serializer_class = UserSerializer
    queryset = Event.objects.all()

class UserCreate(CreateAPIView):
    serializer_class = UserSerializer
    queryset = Event.objects.all()

class UserRetrieve(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = Event.objects.all()

class UserEventsList(ListAPIView):
    def get(self, request):
        user_events = UsersEvents.objects.filter(user_id=request.user.id)
        serializer = UserEventsSerializer(user_events, many=True)
        return Response({"user_events": serializer.data})

class RegisterUserOnEvent(views.APIView):
    def post(self, request):
        event_id = request.data.get('event')
        event = Event.objects.get(id=event_id)
        user_event = UsersEvents.objects.create(user_id=request.user, event_id=event)
        user_event.save()

        return Response({"Success": "Registration user on event {} done succesfully".format(user_event.id)})

class DeleteUserEvent(DestroyAPIView):
    serializer_class = UserOnEventSerializer
    queryset = UsersEvents.objects.all()
