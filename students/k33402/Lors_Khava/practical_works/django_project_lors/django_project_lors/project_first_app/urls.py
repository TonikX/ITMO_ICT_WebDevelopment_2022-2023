from django.urls import path 
from . import views

urlpatterns = [
    path('owner/<int:owner_id>/', views.owner), 
    path('owners/', views.owners), 
    path('owner_create/', views.create_owner),
    path('car_list/', views.CarList.as_view()),
    path('car/<int:pk>/update/', views.CarUpdate.as_view()),
    path('car_create/', views.CarCreate.as_view()),
    path('owner/<int:pk>/delete/', views.CarDelete.as_view())
]