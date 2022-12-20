from .serializers import *
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, \
    DestroyAPIView
from .models import *


# Create your views here.
class EventListAPIView(ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class EventCreateAPIView(CreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()


class UserListAPIView(ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()


class EventRetrieveAPIView(RetrieveAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class UserRetrieveAPIView(RetrieveAPIView):
    serializer_class = UserRetrieveSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = UserUpdateSerializer
    queryset = User.objects.all()


class EnrollCreateAPIView(CreateAPIView):
    serializer_class = UsersEventSerializer
    queryset = UserEnrolledEvent.objects.all()


class UserEnrolledEventAPIView(ListAPIView):
    serializer_class = UserEventsSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Comment.objects.filter(user__id=user_id)


class EventCommentsAPIView(ListAPIView):
    serializer_class = EventCommentSerializer

    def get_queryset(self):
        event_id = self.kwargs['event_id']
        return Comment.objects.filter(event__id=event_id)


class EnrollListAPIView(ListAPIView):
    serializer_class = UsersEventSerializer
    queryset = UserEnrolledEvent.objects.all()


class DeleteEnrolledEventAPIView(DestroyAPIView):
    serializer_class = UsersEventSerializer
    queryset = UserEnrolledEvent.objects.all()


class CommentCreateAPIView(CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentListAPIView(ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentRetrieveAPIView(RetrieveAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class EventsFilterAPIView(ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        type = self.kwargs['type']
        district = self.kwargs['district']
        if type == "all" and district != "all":
            return Event.objects.filter(district=district)
        elif district == "all" and type != "all":
            return Event.objects.filter(type=type)
        elif district == "all" and type == "all":
            return Event.objects.all()
        else:
            return Event.objects.filter(type=type, district=district)
