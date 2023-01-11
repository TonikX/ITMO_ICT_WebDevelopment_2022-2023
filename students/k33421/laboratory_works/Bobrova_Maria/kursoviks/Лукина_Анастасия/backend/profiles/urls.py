from django.urls import path
from .views import *

urlpatterns = [
    path('', ProfileView.as_view(), name='view_profile'),
    path('edit_profile/', ProfileEditView.as_view(), name='edit_profile'),
    path('public-info/<int:pk>/', PublicUserInfo.as_view(), name='public_user_info'),
]