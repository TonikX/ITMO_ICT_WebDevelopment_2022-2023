from django.urls import path
from .views import *

urlpatterns = [
    path('exhibition/', AllExhibition.as_view()),
]