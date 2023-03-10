from django import forms
from django.core.exceptions import ValidationError


class UserValidationForm(forms.ModelForm):
    def save(self, commit=True):
        user = super().save(commit=False)
        if ("password" in self.changed_data):
            user.set_password(self.cleaned_data["password"])
        if commit:
            user.serial_number = user.generate_random_serial()
            user.save()
        return user

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
        reading_room = self.instance
        capacity = self.cleaned_data.get("capacity")
        if capacity is not None:
            users = reading_room.get_all_users()

            if users.count() > capacity:
                raise ValidationError(
                    "The amount of readers cannot exceed the capacity of the room")


class BookValidationForm(forms.ModelForm):
    def clean(self):
        super(BookValidationForm, self).clean()
        book = self.instance
        if book:
            prev_total_stock = book.total_stock
            new_total_stock = self.cleaned_data.get("total_stock")
            if new_total_stock is not None:
                stock_diff = new_total_stock - prev_total_stock

                prev_undesignated_stock = book.get_undesignated_stock()
                new_undesignated_stock = prev_undesignated_stock + stock_diff

                if new_undesignated_stock < 0:
                    raise ValidationError(
                        "The amount of books designated to reading rooms cannot exceed the total stock")


class ReadingRoomBookValidationForm(forms.ModelForm):
    def clean(self):
        super(ReadingRoomBookValidationForm, self).clean()
        reading_room_book = self.instance
        if hasattr(reading_room_book, 'book'):
            book = reading_room_book.book
        else:
            book = self.cleaned_data.get("book")

        prev_stock = reading_room_book.stock
        new_stock = self.cleaned_data.get("stock")

        if new_stock is not None:
            stock_diff = new_stock - prev_stock

            prev_undesignated_stock = book.get_undesignated_stock()
            new_undesignated_stock = prev_undesignated_stock - stock_diff

            if stock_diff > 0 and new_undesignated_stock < 0:
                raise ValidationError(
                    "Not enough undesignated books to restock this reading room")

            prev_avaliable_stock = reading_room_book.get_avaliable_stock()
            new_avaliable_stock = prev_avaliable_stock + stock_diff

            if stock_diff < 0 and new_avaliable_stock < 0:
                raise ValidationError(
                    "The reduction in stock exceeds the avaliable stock")


class ReadingRoomBookUserValidationForm(forms.ModelForm):
    def clean(self):
        super(ReadingRoomBookUserValidationForm, self).clean()
        prev_returned_date = self.instance.returned_date

        reading_room_book = self.cleaned_data.get("reading_room_book")
        new_returned_date = self.cleaned_data.get("returned_date")
        is_trying_to_borrow = new_returned_date is None and prev_returned_date is not None

        if reading_room_book and is_trying_to_borrow:
            if reading_room_book.get_avaliable_stock() < 1:

                raise ValidationError(
                    "This book is out of stock in this reading room")
