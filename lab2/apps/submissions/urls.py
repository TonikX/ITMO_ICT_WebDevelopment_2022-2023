from django.urls import path

from apps.submissions.views import ListSubmissionsView, send_submission

urlpatterns = [
    path('', ListSubmissionsView.as_view(), name='submissions'),
    path('send/<int:hw_id>', send_submission, name='submit')
]
