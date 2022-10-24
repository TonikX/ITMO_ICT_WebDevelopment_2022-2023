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
    path('comments/', views.commentlist),
    path('createcomment/', CreateComment.as_view()),
    path('tours/', views.tourlist),
    path('tours/<int:pk>/reservation', CreateReservation.as_view(), name='reservation'),
    path('profilereservations/', listreservations.as_view(), name='reservations'),
    path('profilereservations/deletereservation/<int:pk>/', views.DeleteReserveView.as_view()),
    path('profilereservations/updatereservation/<int:pk>/', views.UpdateReserveView.as_view())
]



