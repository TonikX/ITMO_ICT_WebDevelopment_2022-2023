from django.urls import path
from . import views

urlpatterns = [
    path('tour/<int:tour_id>', views.show_tour),
    path('tour/registered/<int:tour_id>', views.tours_registered),
    path('tour/registered', views.All_Tours_Registered.as_view()),
    path('tour/', views.All_Tours.as_view()),
    path('reservation_create/', views.Make_Reservation.as_view()),
    path('tour/<int:tour_id>/new_comment', views.Leave_Comment.as_view()),
    path('reservation/<int:pk>/edit/', views.Edit_Reservation.as_view()),
    path('tour/<int:tour_id>/comments/', views.All_Comments.as_view()),
    path('reservation/<int:pk>/delete/', views.Delete_Reservation.as_view()),
    path('accounts/register/', views.register),
    path('accounts/login/', views.user_login),
    path('home/', views.Home.as_view()),
    path('home/registered/', views.Tourist_Page.as_view()),
    path('home/<int:tourist_id>/reservation', views.All_Reservations.as_view()),
    path('accounts/logout', views.logout_user),
    path('tour/registered/<int:tour_id>/comments/', views.All_Comments_Registered.as_view()),
    path('filter/registered/<int:pk>', views.tour_filter_registered),
    path('filter/<int:pk>', views.tour_filter)
]