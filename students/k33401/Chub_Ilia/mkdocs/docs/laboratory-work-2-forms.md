- регистрация
``` python
class RegistrationForm(UserCreationForm):
    class Meta:
        model = BaseUserModel
        fields = ("username", "first_name", "last_name")
```
- подтверждение домашнего задания
``` python
class SubmitHomeworkTaskForm(Form):
    homework_uuid = UUIDField()
    answer = CharField(label="Your answer", max_length=1000)

    class Meta:
        model = SubmitHomeworkTaskModel
        fields = ("homework_uuid", "answer")
```
