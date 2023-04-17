from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('tickets/', views.tickets.as_view(), name="tickets"),
    path('flight/<int:pk>/', views.flight, name="flight"),
    path('ticket/change/<int:pk>/', views.tickets_change.as_view(), name="tic_ch"),
    path('ticket/delete/<int:pk>/', views.tickets_delete.as_view(), name="tic_del"),
    path('signup/', views.SignUp.as_view(), name='signup'),
]
