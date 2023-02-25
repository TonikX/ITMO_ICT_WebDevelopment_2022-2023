from django.urls import path 
from .views import *
urlpatterns = [
    path('', FlightsList.as_view()),
    path('register/', UserRegister.as_view()),
    path('login/', LoginUser.as_view()),
    path('logout/', logout_user),
    path('book/<id_flight>', book_flight),
    path('my_bookings/', BookingsList.as_view()),
    path('my_bookings/<int:pk>/update/', BookingUpdate.as_view()),
    path('my_bookings/<int:pk>/delete/', BookingDelete.as_view()),
    path('passengers/<id_flight>', PassengersList.as_view()),
    path('reviews', ReviewsList.as_view()),
    path('reviews/create/', review_create),
]
#     path('owner/<int:id_owner>', car_owner_info),
#     path('owners_list/', list_view_owners),
#     path('cars_list/', CarsList.as_view()),
#     path('car/<int:pk>/', CarInfo.as_view()),
#     path('owner_create', create_owner_view),
#     path('car/<int:pk>/update/', CarUpdateView.as_view()),
#     path('car/create/', CarCreateView.as_view()),
#     path('car/<int:pk>/delete/', CarDeleteView.as_view()),  
# ]