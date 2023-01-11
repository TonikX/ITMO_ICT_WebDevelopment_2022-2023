from django.urls import path
from project_first_app.views import *

urlpatterns = [
    path('owner/<int:id_owner>', details),
    path('list_owners/', owners_list),
    path('list_cars/', CarsListView.as_view()),
    path('car/<int:pk>', CarRetrieveView.as_view()),
    path('create_owner/', create_owner),
    path('update_car/<int:pk>', CarUpdateView.as_view()),
    path('create_car/', CarCreateView.as_view()),
    path('delete_car/<int:pk>', CarDeleteView.as_view()),
]