from django import forms 
from . models import Student

class StudnetForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        
        widgets = {
            'name' : forms.TextInput(attrs={
                'class' :'myclass',
            }),
            'email' : forms.EmailInput(attrs={
                'class' :'myclass',
            }),
            'password' : forms.PasswordInput(render_value=True, attrs={
                'class' :'myclass',
            }),
        }