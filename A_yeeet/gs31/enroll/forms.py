from django import forms 

class StudentRegistration(forms.Form):
    name = forms.CharField(initial='ferdous', help_text='Enter your name')
    