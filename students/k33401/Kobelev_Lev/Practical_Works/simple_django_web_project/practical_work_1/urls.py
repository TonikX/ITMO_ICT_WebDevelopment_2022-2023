from django.urls import path
from .views import *

urlpatterns = [
    # owner urls
    path('owner/', get_all_owners),
    path('owner/<int:owner_id>/', get_owner),
    path('owner/create', create_owner),

    # car urls
    path('car/', Cars.as_view()),
    path('car/create/', CarCreate.as_view()),
    path('car/<int:pk>/', CarView.as_view()),
    path('car/<int:pk>/update', CarUpdate.as_view()),
    path('car/<int:pk>/delete', CarDelete.as_view()),
]
