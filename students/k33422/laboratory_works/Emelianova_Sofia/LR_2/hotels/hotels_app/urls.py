from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', Homepage.as_view()), # homepage
    path('register/', register, name='register'),  # create user
    path('login/', login_, name='login'),  # login user
    path('logout/', logout_, name='logout'), # logout


    path('hotel/', HotelList.as_view()), # hotel list
    path('hotel/<str:pk>', views.HotelRetriveView, name='HotelRetriveView'), # view
    path('hotel/review/<str:pk>', views.add_comment, name='add_comment'),  # write review


    path('reservation/', ListReservation.as_view()), # reservation list
    path('reservation/create/<str:pk>', views.reservation_create, name='reservation_create'),  # create
    path('reservation/<int:pk>', ReservationRetrieveView.as_view()),  # view
    path('reservation/<int:pk>/update/', ReservationUpdateView.as_view(success_url='/reservation/')),  # edit
    path('reservation/<int:pk>/delete/', ReservationDeleteView.as_view(success_url='/reservation/')),  # delete


    path('guests/', GuestsList.as_view()), #guests list
    ]