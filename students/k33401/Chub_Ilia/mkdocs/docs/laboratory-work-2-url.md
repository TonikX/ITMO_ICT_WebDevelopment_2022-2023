В `laboratory_work_2/urls.py`:

``` python
urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('', include('homework_board_app.urls'))
]
```

В `homework_board_app/urls.py`:

``` python
urlpatterns = [
    re_path('registration',  RegistrationView.as_view()),
    re_path('login', LoginBaseView.as_view(), name="login"),
    re_path('logout', LogoutBaseView.as_view(), name="logout"),
    re_path('homework_tasks/all', AllHomeworkTasksView.as_view()),
    re_path('homework_tasks/submit', SubmitHomeworkTaskView.as_view()),
    re_path('educational_journal', EducationalJournalModel.as_view())
]
```
