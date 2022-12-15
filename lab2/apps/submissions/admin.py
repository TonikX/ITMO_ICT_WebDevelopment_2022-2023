from django.contrib import admin

# Register your models here.
from apps.submissions.models import Submission

admin.site.register(Submission)
