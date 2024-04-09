from django import forms 
from django.core import validators

def starts_with_s(value):
    if value[0] != 's':
        raise forms.ValidationError('First character must start with s')

class StudentRegistration(forms.Form):
    name = forms.CharField(validators=[starts_with_s])
    email = forms.EmailField()
    
    