from django import forms
from .models import *

class StudentForms(forms.Form):
    first_name = forms.CharField(max_length=10)
    last_name = forms.CharField(max_length=10)

class StudentFormModel(forms.ModelForm):
    class Meta :
        model = Eleve
        fields = '__all__' 

