from django import forms


class createLoungeForm(forms.Form):
    lounge_number = forms.CharField(max_length=100)
    lounge_description = forms.CharField(max_length=300)
    lounge_students = forms.CharField(max_length=3)