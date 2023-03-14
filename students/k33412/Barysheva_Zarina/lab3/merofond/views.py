from .serializers import *
from .models import *
from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.db.models.query import EmptyQuerySet


class UsersViewSet(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = MeroUserSerializer

class UserAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MeroUserSerializer

    def get_queryset(self):
        cur_user = self.kwargs['user_id']
        return User.objects.get(pk=cur_user)


class EventAPIView(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        cur_event = self.kwargs['event_id']
        return Event.objects.filter(pk=cur_event)

class EventCreateAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventFilterListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EventSerializer

    def get_queryset(self):
        cur_type = self.kwargs['type']
        cur_location = self.kwargs['location']
        events_cur_type = Event.objects.filter(event_type__title=cur_type)
        events_cur_location = Event.objects.filter(location__title=cur_location)
        if events_cur_location.exists() and events_cur_type.exists():
            return events_cur_location.intersection(events_cur_type)
        if events_cur_location.exists() or events_cur_type.exists():
            return events_cur_location.union(events_cur_type)
        
        return Event.objects.all()   


class EventTypeAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EventTypeSerializer
    def get_queryset(self):
        cur_type = self.kwargs['type_id']
        return EventType.objects.filter(id=cur_type)


class EventTypeListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer

class LocationAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LocationSerializer
    def get_queryset(self):
        cur_location = self.kwargs['location_id']
        return Location.objects.filter(pk=cur_location)

class LocationListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class RegisrationForUserListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EventSerializer

    def get_queryset(self):
        cur_user = self.kwargs['user_id']
        regs = Registration.objects.filter(user__id=cur_user)
        events_id = []
        for reg in regs:
            events_id.append(reg.event.pk)
        return Event.objects.filter(pk__in=events_id)
    
class RegisrationForEventListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MeroUserSerializer

    def get_queryset(self):
        cur_event = self.kwargs['event_id']
        regs = Registration.objects.filter(event__id=cur_event)
        users_id = []
        for reg in regs:
            users_id.append(reg.user.pk)
        return User.objects.filter(id__in=users_id)
    
class RegistrationCreateAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
