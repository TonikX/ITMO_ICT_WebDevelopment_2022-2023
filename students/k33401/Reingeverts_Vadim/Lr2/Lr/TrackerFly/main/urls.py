from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('signup/', views.SignUp.as_view(), name="sign_up"),
    path('login/', views.LogIn.as_view(), name="log_in"),
    path('logout/', views.LogOut.as_view(), name="log_out"),
    path('profile/', views.Profile.as_view(), name="profile"),
    path('flights/', views.Flights.as_view(), name="flights"),
    path('flights/<int:pk>', views.FlightDetails.as_view(), name="flight_details"),
    path('flights/reserve/<int:pk>', views.toggle_reserve, name="toggle_reserve"),
    path('flights/passengers/<int:pk>',
         views.FlightPassengers.as_view(), name="flight_passengers"),
    path('flights/reviews/<int:pk>',
         views.FlightReviews.as_view(), name="flight_reviews"),
]
