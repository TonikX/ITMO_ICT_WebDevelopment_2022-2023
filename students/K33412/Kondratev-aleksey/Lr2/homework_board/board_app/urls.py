from django.urls import path
from . import views

urlpatterns = [
    path('', views.StartPageView.as_view()),
    path('accounts/created/', views.NotificationView.as_view()),
    path('accounts/<int:pk>/update/', views.StudentUpdate.as_view()),
    path('profile/', views.ProfilePageView.as_view()),
    path('profile/all_tasks/', views.AllTasks.as_view()),
    path('profile/all_tasks/answer', views.solution_create),
    path('profile/class_marks/subject_select', views.subject_select),
    path('profile/class_marks', views.class_marks),
]