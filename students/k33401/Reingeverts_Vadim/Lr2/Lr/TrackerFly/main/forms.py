from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

from . import models


class UserSignUpForm(UserCreationForm):

    class Meta:
        model = models.User

        fields = [
            "first_name",
            "last_name",

            "username",
            "email",
        ]


class FlightReviewForm(forms.ModelForm):

    class Meta:
        model = models.Review

        fields = [
            "title",
            "text",
            "rating",
        ]


class FlightValidationForm(forms.ModelForm):
    def clean(self):
        super(FlightValidationForm, self).clean()
        reservators = self.cleaned_data.get("reservators")
        max_reservations = self.cleaned_data.get("max_reservations")

        if reservators:
            reservators_count = reservators.count()

            if reservators_count > max_reservations:
                raise ValidationError("All seats have already been reserved.")
