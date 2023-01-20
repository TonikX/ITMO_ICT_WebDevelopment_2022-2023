from django.urls import path
from . import views

urlpatterns = [
    path('owner/', views.owner_all),
    path('owner/<int:owner_id>/', views.owner_detail),
    path('car/', views.CarList.as_view()),
    path('car/<int:pk>/', views.CarRetrieveView.as_view()),
    path('create_user', views.create_view),
    path('car/<int:pk>/update/', views.CarUpdateView.as_view()),
    path('car_create', views.CarCreate.as_view(success_url="/car/")),
    path('car/<int:pk>/delete/', views.CarDeleteView.as_view()),
]