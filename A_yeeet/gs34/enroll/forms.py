from django import forms 

class StudentRegistration(forms.Form):
    name = forms.CharField(label='Your name ', label_suffix=' ', initial='MD. Tahsin Ferdous', required=False, disabled=True, help_text='Enter your full name ')
    
    
    # if you set the initial value from the 
    # view function (passing it as an argument to the 
    # form class), it will override the initial value
    # that has been setted in forms.py