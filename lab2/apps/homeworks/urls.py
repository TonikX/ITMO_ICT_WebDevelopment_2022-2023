from django.urls import path

from apps.homeworks.views import HomeworksView

urlpatterns = [
    path('', HomeworksView.as_view(), name='home')
]