from django.urls import path

from work_space.views import TaskCreate, TaskList, AnswerCreate, AnswerList


app_name = 'work'


urlpatterns = [
    path('task_create/', TaskCreate, name='task_create'),
    path('task_list/', TaskList, name='task_list'),
    path('task_answer/<int:pk>/', AnswerCreate, name='task_answer'),
    path('answer_list/', AnswerList, name='task_list')
]
