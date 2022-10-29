from django import forms


class ReserveForm(forms.Form):
    start_at = forms.DateTimeField()
    end_at = forms.DateTimeField()


class MoveReserveForm(forms.Form):
    start_at = forms.DateTimeField()
    end_at = forms.DateTimeField()


class DeleteReserveForm(forms.Form):
    is_delete = forms.BooleanField()


class AddComment(forms.Form):
    rate = forms.IntegerField(min_value=1, max_value=10)
    comment = forms.CharField()
