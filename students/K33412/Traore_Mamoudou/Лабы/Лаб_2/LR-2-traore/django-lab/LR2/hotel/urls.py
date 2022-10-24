from .views import *
from django.urls import path
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('hotels/', ListHotels.as_view(), name='hotels'),
    path('hotels/<int:pk>/', ListHotelRooms.as_view()),
    path('rooms/<int:pk>/book', CreateBooking.as_view(), name='booking'),
    path('register/', registration),
    path('login/', LoginView.as_view(template_name='login.html')),
    path('logout/', logout_view),
    path('account/login/', profile, name='profile'),
    path('profile/bookings', ListBookings.as_view(), name='bookings'),
    path('profile/bookings/delete/<int:pk>/', DeleteBooking.as_view(), name='delete_booking'),
    path('reviews/', ListReviews.as_view(), name='review_list'),
    path('rooms/<int:pk>/add_review', CreateReview.as_view(), name='add_review'),
    path('last_guests/', ListGuests.as_view(), name='last_guests')
]