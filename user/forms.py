from django import forms
from .models import *


class UserForms(forms.Form):
    first_name = forms.CharField(max_length=10)
    last_name = forms.CharField(max_length=10)
    created_at = forms.DateField()


class UserFormsModel(forms.ModelForm):
    class Meta:
        model = User 
        # fields = "__all__"
        exclude = ["created_at"]

