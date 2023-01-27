from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('owner/<int:id_owner>/', views.owner_detail),
    path('owner/', views.owner_list),
    path('owner/create', views.owner_create),
    path('car/<int:pk>/', views.CarDetail.as_view()),
    path('car/', views.CarList.as_view()),
    path('car/<int:pk>/update/', views.CarUpdate.as_view()),
    path('car/create/', views.CarCreate.as_view(success_url="/car/")),
    path('car/<int:pk>/delete/', views.CarDelete.as_view()),
]