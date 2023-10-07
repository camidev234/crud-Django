from django import forms


class createTeacherForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    lastname = forms.CharField(max_length=300, required=True)
    age = forms.CharField(required=True)
    email = forms.EmailField(max_length=150, required=True)