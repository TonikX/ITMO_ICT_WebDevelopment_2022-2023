from django.urls import path 
from .views import *

urlpatterns = [
    path('car/list/', CarList.as_view()),
    path('car/list/create/', CarCreateView.as_view()),
    path('car/<int:pk>/', CarViev.as_view()),
    path('car/<int:pk>/update', CarUpdateView.as_view()),
    path('car/<int:pk>/delete/', CarDeleteView.as_view()),
    path('owner/<int:pk>/', owner),
    path('owners/', owners),
]