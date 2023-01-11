from django.urls import path
from .views import *

urlpatterns = [
    path('owner/<int:owner_id>', owner),
    path('owner/list/', list_owners),
    path('auto/list/', AutoList.as_view()),
    path('auto/create/', AutoCreate.as_view()),
    path('auto/<int:pk>/update/', AutoUpdate.as_view()),
    path('auto/<int:pk>/delete/', AutoDelete.as_view()),
    path('owner/create/', owner_create),
]