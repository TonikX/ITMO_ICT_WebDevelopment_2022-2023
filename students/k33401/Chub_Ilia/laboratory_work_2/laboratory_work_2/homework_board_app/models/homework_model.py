from . import *


class HomeworkModel(Model):
    uuid = UUIDField(primary_key=True, default=uuid4, editable=False)
    academic_discipline = ForeignKey(AcademicDisciplineModel, on_delete=CASCADE)
    start_date = DateField("Start date")
    end_date = DateField("End date")
    description = CharField("Description", max_length=1000)
    fine_for_being_late = IntegerField("Fine for being late")
