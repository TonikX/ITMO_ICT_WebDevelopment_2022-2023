- Все домашние задания текущего студента
``` python
class AllHomeworkTasksView(LoginRequiredMixin, ListView):
    model = HomeworkModel
    template_name = "all_homework_tasks_template.html"

    def get_queryset(self):
        queryset = self.queryset

        try:
            student = StudentModel.objects.get(user__username=self.request.user.username)
            queryset = self.model.objects.filter(academic_discipline__students_uuids=student.id)
        except:
            pass

        return queryset
```
- Отметки текущего студента за домашние задания
``` python
class EducationalJournalModel(ListView):
    model = EducationalJournalModel
    template_name = "all_educational_journal_template.html"

    def get_queryset(self):
        queryset = self.queryset

        try:
            student = StudentModel.objects.get(user__username=self.request.user.username)
            queryset = self.model.objects.filter(submit_homework_task_uuid__student_id=student.id)
        except:
            pass

        return queryset
```
- Вход
``` python
class LoginBaseView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login_template.html'
```
- Выход
``` python
class LogoutBaseView(LoginRequiredMixin, LogoutView):
    next_page = 'login'
```
- Регистрация
``` python
class RegistrationView(SuccessMessageMixin, CreateView):
    success_url = reverse_lazy('login')
    form_class = RegistrationForm
    success_message = "Success"
    template_name = "registration_template.html"
```
- Загрузка домашнего задания для проверки
``` python
class SubmitHomeworkTaskView(LoginRequiredMixin, FormView):
    form_class = SubmitHomeworkTaskForm
    template_name = 'submit_homework_task_template.html'
    success_url = 'homework_tasks/all'

    def form_valid(self, form):
        user = self.request.user
        student_model = StudentModel.objects.get(user=user)
        uuid = form.cleaned_data['homework_uuid']
        answer = form.cleaned_data['answer']
        homework_model = HomeworkModel.objects.get(uuid=uuid)
        submitHomeworkTaskModel = SubmitHomeworkTaskModel(
            homework_uuid=homework_model,
            answer=answer,
            student_id=student_model
        )

        submitHomeworkTaskModel.save()

        return super(SubmitHomeworkTaskView, self).form_valid(form)
```
