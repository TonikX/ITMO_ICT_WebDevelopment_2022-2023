from django.urls import path
from .views import *

urlpatterns = [
    path('owners/<int:owner_id>', owner),
    path('cars/<int:car_id>', car),
    path('cars', CarsList.as_view()),
    path('owners', OwnersList.as_view()),
    path('create_car', createCar),
    path('owners/<int:pk>/update/', OwnerUpdateView.as_view()),
    path('cars/<int:pk>/update/', CarUpdateView.as_view()),
    path('create_owner', OwnerCreateView.as_view()),
    path('owners/<int:pk>/delete/', OwnerDeleteView.as_view()),
    path('cars/<int:pk>/delete/', CarDeleteView.as_view()),
]
