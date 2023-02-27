from . import *


class AcademicDisciplineModel(Model):
    uuid = UUIDField(primary_key=True, default=uuid4, editable=False)
    title = CharField(max_length=100, blank=True, null=True)
    students_uuids = ManyToManyField(StudentModel)
