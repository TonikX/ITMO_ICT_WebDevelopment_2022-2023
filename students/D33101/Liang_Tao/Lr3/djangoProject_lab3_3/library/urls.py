from django.urls import path
from .views import *


app_name = "online_store"


urlpatterns = [
    path('users/', UserAPIView.as_view()),
    path('books/<int:pk>',BoolAPIView.as_view()),
    path('add/book/',BookCreateAPIView.as_view()),
    path('records/',RecordAPIView.as_view()),
]