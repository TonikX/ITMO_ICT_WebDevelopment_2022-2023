from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('login', views.CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(
        next_page='hotels'), name='logout'),
    path('register', views.RegisterPage.as_view(), name='register'),
    path('', views.HotelsList.as_view(), name='hotels'),
    path('hotel/<int:hotel_id>', views.hotel_detail, name='hotel'),
    path('hotel/<int:hotel_id>/room/<int:room_id>',
         views.room_detail, name='room'),
    path('hotel/<int:hotel_id>/room/<int:room_id>/reservation',
         views.reservation_view, name='room_reservation'),
    path('reservation', views.ReservationList.as_view(), name='reservations'),
    path('reservation/delete/<int:pk>',
         views.DeleteReservationView.as_view(), name='reservation_delete'),

]
