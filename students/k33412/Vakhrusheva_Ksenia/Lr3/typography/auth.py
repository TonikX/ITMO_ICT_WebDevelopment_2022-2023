import typing

from rest_framework import authentication
from rest_framework import exceptions
from rest_framework.request import Request

from .models import UserProfile, Author, Manager, Editor, Customer


class MultiUserProfileAuthentication(authentication.TokenAuthentication):
	strict = True
	user_profile_models: typing.List[UserProfile] = []

	def authenticate(self, request: Request):
		token_authentication = super().authenticate(request)
		if not token_authentication:
			return None

		user, token = token_authentication
		profile = None
		for user_profile_model in self.user_profile_models:
			try:
				profile = user_profile_model.objects.get(user=user)
				return user, profile
			except user_profile_model.DoesNotExist:
				pass

		if profile is None:
			if self.strict:
				raise exceptions.AuthenticationFailed(f'No profiles for this user')
			else:
				return token_authentication


class AMEProfilesAuthentication(MultiUserProfileAuthentication):
	user_profile_models = [Manager, Editor, Author]


class MCProfilesAuthentication(MultiUserProfileAuthentication):
	user_profile_models = [Manager, Customer]


class MEProfilesAuthentication(MultiUserProfileAuthentication):
	user_profile_models = [Manager, Editor]


class UserProfileAuthentication(authentication.TokenAuthentication):
	strict = True
	user_profile_model: UserProfile = None

	def authenticate(self, request: Request):
		token_authentication = super().authenticate(request)
		if not token_authentication:
			return None

		user, token = token_authentication
		try:
			profile = self.user_profile_model.objects.get(user=user)
		except self.user_profile_model.DoesNotExist:
			if self.strict:
				raise exceptions.AuthenticationFailed(f'No {self.user_profile_model.__name__} profile for this user')
			else:
				return token_authentication

		return user, profile


class AuthorAuthentication(UserProfileAuthentication):
	user_profile_model = Author


class ManagerAuthentication(UserProfileAuthentication):
	user_profile_model = Manager


class NonStrictManagerAuthentication(UserProfileAuthentication):
	strict = False
	user_profile_model = Manager


class EditorAuthentication(UserProfileAuthentication):
	strict = False
	user_profile_model = Editor


class CustomerAuthentication(UserProfileAuthentication):
	user_profile_model = Customer
