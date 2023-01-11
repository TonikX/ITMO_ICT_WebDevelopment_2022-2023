from django import forms


class RegForm(forms.Form):
    text = forms.CharField()


class ChangeRegForm(forms.Form):
    new_text = forms.CharField()


class DeleteRegForm(forms.Form):
    is_delete = forms.BooleanField()


class AddComment(forms.Form):
    rate = forms.IntegerField(min_value=1, max_value=10)
    comment = forms.CharField()
