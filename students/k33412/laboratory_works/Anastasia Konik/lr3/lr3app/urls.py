from django.urls import path, re_path
from .views import *

app_name = "lr3app"

urlpatterns = [
    path('events/list/', EventListAPIView.as_view()),
    path('event/<int:pk>/', EventRetrieveAPIView.as_view()),
    path('event/create/', EventCreateAPIView.as_view()),
    path('event/update/<int:pk>/', EventUpdateAPIView.as_view()),
    path('users/list/', UserListAPIView.as_view()),
    path('user/<int:pk>/', UserRetrieveAPIView.as_view()),
    path('user/create/', UserCreateAPIView.as_view()),
    path('user/delete/<int:pk>/', UserDestroyAPIView.as_view()),
    path('user/edit/<int:pk>/', UserUpdateAPIView.as_view()),
    path('enroll/create/', EnrollCreateAPIView.as_view()),
    path('enroll/delete/<int:pk>/', DeleteEnrolledEventAPIView.as_view()),
    path('enroll/list/', EnrollListAPIView.as_view()),
    path('comments/list/', CommentListAPIView.as_view()),
    path('comment/create/', CommentCreateAPIView.as_view()),
    path('comment/<int:pk>/', CommentRetrieveAPIView.as_view()),
    re_path(r'event/comments/(?P<event_id>[0-9]+)/$', EventCommentsAPIView.as_view()),
    re_path(r'user/events/(?P<user_id>[0-9]+)/$', UserEnrolledEventAPIView.as_view()),
    re_path(r'events/filter/(?P<type>\w*)/(?P<district>\w*)/$', EventsFilterAPIView.as_view())
]
