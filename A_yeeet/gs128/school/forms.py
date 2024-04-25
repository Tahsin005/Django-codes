from django import forms 
from . models import Student

class StudnetForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'password']
        widgets = {
            'name' : forms.TextInput(attrs={
                'class' : 'myclass',
            }),
            'password' : forms.PasswordInput(attrs={
                'class' : 'mypassword',
            }),
        }

        