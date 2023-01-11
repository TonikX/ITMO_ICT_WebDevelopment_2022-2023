from django.urls import path
from .views import *

urlpatterns = [
    path('', AllExhibition.as_view()),
]