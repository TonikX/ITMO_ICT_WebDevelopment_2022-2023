from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('hotels/', ListHotels.as_view(), name='hotels'),
    path('rooms/', ListRooms.as_view(), name='rooms'),
    path('hotels/<int:pk>/', ListHotelRooms.as_view()),
    path('rooms/<int:pk>/', RoomDetail.as_view()),
    path('rooms/<int:pk>/book', CreateBooking.as_view(), name='booking'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('profile/edit', edit_profile, name='edit_profile'),
    path('profile/bookings', ListBookings.as_view(), name='bookings'),
    path('profile/bookings/delete/<int:pk>/', DeleteBooking.as_view(), name='delete_booking'),
    path('reviews/', ListReviews.as_view(), name='review_list'),
    path('rooms/<int:pk>/add_review', CreateReview.as_view(), name='add_review'),
    path('last_guests/', ListGuests.as_view(), name='last_guests')

]