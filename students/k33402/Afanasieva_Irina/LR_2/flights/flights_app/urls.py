from django.urls import path

from .views import *

urlpatterns = [
    path('user/register/', UserCreateView.as_view()),  # create user
    path('user/<int:pk>/', UserRetrieveView.as_view()),  # view user

    # reservation
    path('reservation/create', ReservationCreateView.as_view()),  # create
    path('reservation/<int:pk>', ReservationRetrieveView.as_view()),  # view
    path('reservation/edit/<int:pk>', ReservationUpdateView.as_view()),  # edit
    path('reservation/delete/<int:pk>', ReservationDeleteView.as_view()),  # delete

    path('flight/<int:pk>', PassengerList.as_view()),  # list passengers on specified flight

    path('review', ReviewCreateView.as_view()),  # write review

    path('success', success),
]
