from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('owner/<int:id_owner>/', views.owner_information),
    path('all_owners/', views.return_all_owners),
    path('all_cars/', CarListView.as_view()),
    path('car/<int:pk>', CarDetailView.as_view()),
    path('create_owner/', create_owner),
    path('update_car/<int:pk>', CarUpdate.as_view()),
    path('create_car/', CarCreate.as_view()),
    path('delete_car/<int:pk>', CarDelete.as_view()),
]