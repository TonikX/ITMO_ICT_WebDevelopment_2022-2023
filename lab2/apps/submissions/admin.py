from django.contrib import admin
# Register your models here.
from django.utils import timezone

from apps.submissions.models import Submission


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('homework', 'student', 'mark', 'submitted_at', 'checked_at')
    list_filter = ('homework', 'student')

    def save_model(self, request, obj, form, change):
        obj.checked_at = timezone.now()
        super().save_model(request, obj, form, change)


admin.site.register(Submission, SubmissionAdmin)
