from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('users/', UsersViewSet.as_view()),
    path('event/create/', EventCreateAPIView.as_view()),
    path('event/list/', EventListAPIView.as_view()),
    re_path(r'event/(?P<event_id>[0-9]+)/$', EventAPIView.as_view()),
    re_path(r'event/list/filter/(?P<type>\w*)/(?P<location>\w*)/$', EventFilterListAPIView.as_view()),
    path('event/type/', EventTypeListAPIView.as_view()),
    re_path(r'event/type/(?P<type_id>[0-9]+)/$', EventTypeAPIView.as_view()),
    re_path(r'event/location/(?P<location_id>[0-9]+)/$', LocationAPIView.as_view()),
    path('event/location/', LocationListAPIView.as_view()),
    re_path(r'user/(?P<user_id>[0-9]+)/$', UserAPIView.as_view()),
    re_path(r'user/(?P<user_id>[0-9]+)/events/$', RegisrationForUserListAPIView.as_view()),
    re_path(r'event/(?P<event_id>[0-9]+)/users/$', RegisrationForEventListAPIView.as_view()),
    path('event/reg/', RegistrationCreateAPIView.as_view()),
]