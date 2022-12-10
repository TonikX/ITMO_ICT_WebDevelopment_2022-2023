from django.urls import path
from .views import *

urlpatterns = [
    path('owner/<int:owner_id>', details),
    path('owners_list/', owners_list),
    path('create_owner/', create_owner),
    path('car/<int:pk>', CarRetrieveView.as_view()),
    path('cars_list/', CarsListView.as_view()),
    path('create_car/', CarCreateView.as_view()),
    path('update_car/<int:pk>', CarUpdateView.as_view()),
    path('delete_car/<int:pk>', CarDeleteView.as_view()),
]
