from django.urls import path

from apps.homeworks.views import ListHomeworksView

urlpatterns = [
    path('', ListHomeworksView.as_view(), name='home')
]