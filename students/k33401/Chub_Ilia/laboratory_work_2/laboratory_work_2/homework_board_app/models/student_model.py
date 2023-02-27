from . import *


class StudentModel(Model):
    user = ForeignKey(BaseUserModel, on_delete=CASCADE)
