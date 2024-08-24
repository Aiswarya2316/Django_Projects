from django import forms
from .models import *

class user_std(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    mark = forms.IntegerField()

class model_form(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        widgets={
            'age':forms.NumberInput(attrs={'class':'form-controller bg-info'}),

        }