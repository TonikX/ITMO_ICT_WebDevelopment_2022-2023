from . import *
from django.contrib.auth.models import AbstractUser


class BaseUserModel(AbstractUser):
    uuid = UUIDField(primary_key=True, default=uuid4, editable=False)
