from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('owner/<int:id_owner>/', views.info_about_car_owner),
    path('list_owners/', views.all_owners),
    path('list_cars/', CarList.as_view()),
    path('car/<int:pk>', CarById.as_view()),
    path('create_owner/', create_owner),
    path('update_car/<int:pk>', CarUpdate.as_view()),
    path('create_car/', CarCreate.as_view()),
    path('delete_car/<int:pk>', CarDelete.as_view()),
]