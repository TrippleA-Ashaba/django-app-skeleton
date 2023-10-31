from django import forms


class SampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    age = forms.IntegerField(min_value=18, max_value=100)
    gender = forms.ChoiceField(choices=(("M", "Male"), ("F", "Female")))
    date_of_birth = forms.DateField()
