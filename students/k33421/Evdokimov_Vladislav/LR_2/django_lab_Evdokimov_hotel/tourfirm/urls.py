from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('main/', views.homepage),
    path('profile/', views.profile),
    path('login/', views.user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', views.log_out),
    path('reservedtour/', views.reservedtourlist),
    path('commentlist/', views.commentlist),
    path('tours/<int:pk>/createcomment', CreateComment.as_view(), name='comment'),
    path('tours/', views.tourlist),
    path('tours/<int:pk>/reservation', CreateReservation.as_view(), name='reservation'),
    path('profilereservations/', listreservations.as_view(), name='reservations'),
    path('profilereservations/lcreservations/deletereservation/<int:pk>/', views.DeleteReserveView.as_view()),
    path('profilereservations/lcreservations/updatereservation/<int:pk>/', views.UpdateReserveView.as_view())
]



