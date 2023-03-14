from django.contrib import admin
from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('users/<int:pk>', UserRetrieveAPIView.as_view()),
    path('users/update/<int:pk>', UserUpdateAPIView.as_view()),
    path('users/all', UserListAPIView.as_view()),
    path('user/new', UserCreateAPIView.as_view()),

    path('categories/<int:pk>', CategoryRetrieveAPIView.as_view()),
    path('categories/all', CategoryListAPIView.as_view()),
    path('categories/new', CategoryCreateAPIView.as_view()),

    path('locations/<int:pk>', LocationRetrieveAPIView.as_view()),
    path('locations/update/<int:pk>', LocationUpdateAPIView.as_view()),
    path('locations/all', LocationListAPIView.as_view()),
    path('locations/new', LocationCreateAPIView.as_view()),

    path('events/<int:pk>', EventRetrieveAPIView.as_view()),
    path('events/update/<int:pk>', EventUpdateAPIView.as_view()),
    path('events/all', EventListAPIView.as_view()),
    path('events/new', EventCreateAPIView.as_view()),

    path('categories/<int:pk>', CategoryRetrieveAPIView.as_view()),
    path('categories/update/<int:pk>', CategoryUpdateAPIView.as_view()),
    path('categories/all', CategoryListAPIView.as_view()),
    path('categories/new', CategoryCreateAPIView.as_view()),
]