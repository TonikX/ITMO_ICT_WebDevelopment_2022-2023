from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('user/list/', views.UserList.as_view()),
    path('', views.HomeworkList.as_view()),
    path('homework/create/', views.HomeworkCreate.as_view()),
    path('homework/upload/', views.HomeworkUpload.as_view()),
    path('homework/mark/<int:pk>', views.HomeworkMark.as_view()),
    path('student/mark/', views.StudentMarkList.as_view()),
    path('registration/', views.UserCreate.as_view()),
    path('login/', views.user_login),
    path('logout/', LogoutView.as_view()),
]