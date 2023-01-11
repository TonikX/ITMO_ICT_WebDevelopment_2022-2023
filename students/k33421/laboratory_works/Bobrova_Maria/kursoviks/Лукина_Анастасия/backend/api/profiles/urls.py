from django.urls import path
from .views import *

urlpatterns = [
    path('', ProfileUser.as_view()),
    path('update-ava/', UpdateProfile.as_view()),
]

