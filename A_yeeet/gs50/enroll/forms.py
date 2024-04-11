from django import forms 
from django.core import validators
from . models import User

class StudentRegistration(forms.ModelForm):
    name = forms.CharField(max_length=50, required=False) 
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        labels = {
            'name' : 'Enter your name',
            'email' : 'Enter your email address',
            'password' : 'Enter your password'
        }
        help_text = {
            'name' : 'Enter your full name',
            'email' : 'Enter your email address',
            'password' : 'Enter your password',
        }
        error_messages = {
            'name' : {
               'required' : 'Name is required',
            },
            'email' : {
               'required' : 'Email is required',
            },
            'password' : {
               'required' : 'Password is required',
            }
        }
        widgets = {
            'password' : forms.PasswordInput(attrs={
                'placeholder' : 'Password dede bhai',
            }),
            'name' : forms.TextInput(attrs={
                'class' : 'myclass',
                'placeholder' : 'Yaha naam likh'
            })
        }
        