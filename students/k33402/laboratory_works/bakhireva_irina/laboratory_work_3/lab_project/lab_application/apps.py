from django.apps import AppConfig


class LabApplicationConfig(AppConfig):
	default_auto_field = "django.db.models.BigAutoField"
	name = "lab_application"

	def ready(self):
		import lab_application.signals  # noqa
