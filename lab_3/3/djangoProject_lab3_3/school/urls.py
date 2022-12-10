from django.urls import path
from .views import *

app_name = "online_store"

urlpatterns = [
    path('create/users/', User_APIView.as_view()),
    path('change/users/', User_UpdateDestroyAPIView.as_view()),
    path('create/class/', School_class_CreateAPIView.as_view()),
    path('change/class/', School_class_APIView.as_view()),
    path('create/user_class/', Student_class_teacher_CreateAPIView.as_view()),
    path('change/user_class/', SStudent_class_teacher_APIView.as_view()),
]
