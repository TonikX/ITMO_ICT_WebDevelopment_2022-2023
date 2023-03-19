from . import *


class TeacherModel(Model):
    user = ForeignKey(BaseUserModel, on_delete=CASCADE)
