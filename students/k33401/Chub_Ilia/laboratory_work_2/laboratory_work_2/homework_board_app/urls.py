from .views import *
from django.urls import re_path


urlpatterns = [
    re_path('registration',  RegistrationView.as_view()),
    re_path('login', LoginBaseView.as_view(), name="login"),
    re_path('logout', LogoutBaseView.as_view(), name="logout"),
    re_path('homework_tasks/all', AllHomeworkTasksView.as_view()),
    re_path('homework_tasks/submit', SubmitHomeworkTaskView.as_view()),
    re_path('educational_journal', EducationalJournalModel.as_view())
]
