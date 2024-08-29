from django import forms
from . import models


class TeacherForms(forms.Form):
    first_name = forms.CharField(max_length=10)
    last_name = forms.CharField(max_length=10)

class TeacherFormModel(forms.ModelForm):
    class Meta:
        model = models.Teacher
        fields = '__all__'

    
