from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

from . import models


class UserSignUpForm(UserCreationForm):

    class Meta:
        model = models.User

        fields = [
            "username",
            "passport",

            "last_name",
            "first_name",
            "middle_name",

            "address",
            "education_level",
            "phone_number",
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.serial_number = user.generate_random_serial()
            user.save()
        return user


class UserValidationForm(forms.ModelForm):
    def clean(self):
        super(UserValidationForm, self).clean()
        reading_room = self.cleaned_data.get("reading_room")
        if reading_room:
            if reading_room.get_empty_slots() - 1 < 0:
                raise ValidationError(
                    "There is not enough slots in this reading room")


class ReadingRoomValidationForm(forms.ModelForm):
    def clean(self):
        super(ReadingRoomValidationForm, self).clean()
        reading_room = self.save(commit=False)
        capacity = self.cleaned_data.get("capacity")
        users = reading_room.user_set

        print(users.count(), capacity)
        if users.count() > capacity:
            raise ValidationError(
                "The amount of readers cannot exceed the capacity of the room")


class BookValidationForm(forms.ModelForm):
    def clean(self):
        super(BookValidationForm, self).clean()
        book = self.save(commit=False)

        prev_total_stock = book.total_stock
        new_total_stock = self.cleaned_data.get("total_stock")
        stock_diff = new_total_stock - prev_total_stock

        prev_undesignated_stock = book.get_undesignated_stock()
        new_undesignated_stock = prev_undesignated_stock + stock_diff

        if new_undesignated_stock < 0:
            raise ValidationError(
                "The amount of books designated to reading rooms cannot exceed the total stock")


class ReadingRoomBookUserValidationForm(forms.ModelForm):
    def clean(self):
        super(ReadingRoomBookUserValidationForm, self).clean()
        reading_room_book = self.cleaned_data.get("reading_room_book")
        if reading_room_book.get_avaliable_stock() < 1:
            raise ValidationError(
                "This book is out of stock in this reading room")


class ReadingRoomBookValidationForm(forms.ModelForm):
    def clean(self):
        super(ReadingRoomBookValidationForm, self).clean()
        reading_room_book = self.save(commit=False)
        book = self.cleaned_data.get("book")

        prev_stock = reading_room_book.stock
        new_stock = self.cleaned_data.get("stock")
        stock_diff = new_stock - prev_stock

        prev_undesignated_stock = book.get_undesignated_stock()
        new_undesignated_stock = prev_undesignated_stock - stock_diff

        if stock_diff > 0 and new_undesignated_stock < 0:
            raise ValidationError(
                "Not enough undesignated books to restock this reading room")
