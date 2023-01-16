from django.dispatch import receiver
from djoser.signals import user_registered

from lab_application.models import User, ROLE_APPLICANT, Applicant


@receiver(user_registered)
def djoser_registered(user: User, **kwargs):
	if user.role == ROLE_APPLICANT:
		Applicant.objects.create(user=user)
