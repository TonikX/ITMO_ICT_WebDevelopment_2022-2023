from django.urls import path
from django.contrib.auth import views
import tourism.views


urlpatterns = [
    path('', tourism.views.view_table, name='view_table'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('sign_out/', views.LogoutView.as_view(), name='sign_out'),
    path('sign_up/', tourism.views.sign_up, name='sign_up'),
    path('tours/', tourism.views.view_tours, name='view_tours'),
    path('tours/<int:pk>', tourism.views.view_tour, name='view_tour'),
    path('tours/<int:pk>/reserve', tourism.views.reserve_tour, name='reserve_tour'),
    path('reservations/', tourism.views.view_reservations, name='view_reservations'),
    path('reservations/<int:pk>/cancel', tourism.views.cancel_reservation, name='cancel_reservation'),
]