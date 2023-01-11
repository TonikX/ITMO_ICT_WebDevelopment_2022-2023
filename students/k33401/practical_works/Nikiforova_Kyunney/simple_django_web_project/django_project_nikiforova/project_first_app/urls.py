from django.urls import path
from . import views

urlpatterns = [
    path('owner/<int:owner_id>/', views.owner_detail),
    path('all_owners/', views.owner_all),
    path('all_cars/', views.CarList.as_view()),
    path('car/<int:pk>/', views.CarRetrieveView.as_view()),
    path('create_owner/', views.create_owner),
    path('car/<int:pk>/update/', views.CarUpdate.as_view()),
    path('create_car/', views.CarCreate.as_view(success_url="/all_cars/")),
    path('car/<int:pk>/delete/', views.CarDelete.as_view()),
]