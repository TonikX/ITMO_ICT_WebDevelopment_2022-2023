from django.urls import path 
from .views import *
urlpatterns = [
    path('owner/<int:id_owner>', car_owner_info),
    path('owners_list/', list_view_owners),
    path('cars_list/', CarsList.as_view()),
    path('car/<int:pk>/', CarInfo.as_view()),
    path('owner_create', create_owner_view),
    path('car/<int:pk>/update/', CarUpdateView.as_view()),
    path('car/create/', CarCreateView.as_view()),
    path('car/<int:pk>/delete/', CarDeleteView.as_view()),  
]