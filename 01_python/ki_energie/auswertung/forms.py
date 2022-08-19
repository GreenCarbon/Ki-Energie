from django import forms 
from ki_energie.models import Raumliste

class InputForm(forms.Form):
    
    bool_1 = forms.BooleanField(required=False)
    first_name = forms.CharField(max_length=200, label="Erster Name")
    last_name = forms.CharField(max_length=200)
    roll_number = forms.IntegerField(
        help_text="Geben Sie die 6-stellige Rollennummer ein")
    password = forms.CharField(widget=forms.PasswordInput())


class DSP_Raumliste(forms.ModelForm):
    class Meta:
        model = Raumliste
        fields = ('server_name', 'etage', 'raum', 'beschreibung',)
