from django.urls import path

from .views import *

app_name = "gamebazzar"

urlpatterns = [
    path('genre/', GenreListAPIView.as_view()),
    path('platform/', PlatformListAPIView.as_view()),
    path('game/', GameListAPIView.as_view()),
    path('product/', ProductListAPIView.as_view()),
    path('sell/', SellListAPIView.as_view()),
    path('sell/info/', SellSummaryListAPIView.as_view()),

    path('product/<int:pk>/', ProductAPIView.as_view()),
    path('product/<int:pk>/delete/', ProductDeleteAPIView.as_view()),
    path('product/<int:pk>/update/', ProductUpdateAPIView.as_view()),
    path('product/create/', ProductCreateAPIView.as_view()),

    path('me/', UserAPIView.as_view()),
    path('staff/', UserListAPIView.as_view()),
    path('staff/<str:username>/', UserUpdateAPIView.as_view()),
]
