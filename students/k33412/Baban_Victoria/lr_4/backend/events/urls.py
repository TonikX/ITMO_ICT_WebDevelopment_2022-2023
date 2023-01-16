from django.urls import path
from .views import *

urlpatterns = [
    path('events', EventsList.as_view()),
    path('events/<int:pk>', EventRetrieve.as_view()),
    path('users', UserList.as_view()),
    path('users/<int:pk>', UserRetrieve.as_view()),
    path('users_events', UserEventsList.as_view()),
    path('users_events/add', RegisterUserOnEvent.as_view()),
    path('users_events/<int:pk>', DeleteUserEvent.as_view())
]