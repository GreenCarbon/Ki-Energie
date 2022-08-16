from django import forms 


class InputForm(forms.Form):
    
    bool_1 = forms.BooleanField(required=False)
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    roll_number = forms.IntegerField(
    help_text="Enter 6 digit roll number")
    password = forms.CharField(widget=forms.PasswordInput())
