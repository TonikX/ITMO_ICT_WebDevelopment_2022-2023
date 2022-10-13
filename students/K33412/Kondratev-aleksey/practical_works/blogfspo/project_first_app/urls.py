from django.urls import path
from . import views

urlpatterns = [
    path('owner/<int:id_owner>', views.info_about_owner),
    path('list_owners/', views.all_owners)
]