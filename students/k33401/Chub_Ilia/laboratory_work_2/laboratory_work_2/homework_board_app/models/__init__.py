from uuid import uuid4
from django.db.models import \
    Model, CharField, UUIDField, ForeignKey, CASCADE, ManyToManyField, DateField, CharField, IntegerField

from .base_user_model import BaseUserModel
from .student_model import StudentModel
from .teacher_model import TeacherModel
from .academic_discipline import AcademicDisciplineModel
from .homework_model import HomeworkModel
from .educational_journal_model import EducationalJournalModel
from .submit_homework_task_model import SubmitHomeworkTaskModel
