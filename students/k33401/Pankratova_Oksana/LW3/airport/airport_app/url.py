from django.urls import path
from . import views

urlpatterns = [
    path('flight/<int:pk>/', views.FlightAPI.as_view()),
    path('flights/', views.FlightListAPI.as_view()),
    path('employee/<int:pk>/', views.EmployeeAPI.as_view()),
    path('employees/', views.EmployeeListAPI.as_view()),
    path('plane/<int:pk>/', views.PlaneAPI.as_view()),
    path('planes/', views.PlaneListAPI.as_view()),
    path('flight/create/', views.FlightCreateAPI.as_view()),
    path('employee/create/', views.EmployeeCreateAPI.as_view()),
    path('plane/create/', views.PlaneCreateAPI.as_view()),
    path('transit_land/create/', views.TransitLandingCreateAPI.as_view()),
    path('flight/upd_del/<int:pk>/', views.FlightUpdateDeleteAPI.as_view()),
    path('employee/upd_del/<int:pk>/', views.EmployeeUpdateDeleteAPI.as_view()),
    path('plane/upd_del/<int:pk>/', views.PlaneUpdateDeleteAPI.as_view()),
]
