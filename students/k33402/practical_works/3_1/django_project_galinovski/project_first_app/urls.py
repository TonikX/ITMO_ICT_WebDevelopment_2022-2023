
from django.urls import path

from . import views

urlpatterns = [
    path("owner/<int:owner_id>/", views.get_info_owner),
    path("owner/", views.get_all_owners),
]