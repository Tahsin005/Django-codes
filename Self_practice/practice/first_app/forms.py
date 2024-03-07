from django import forms
from django.core import validators

class studentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput, validators=[validators.MinLengthValidator(10, message='Name should be at least 10 characters')])
    files = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf', 'png'], message='We only support pdf files')]) 
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password!= confirm_password:
            raise forms.ValidationError('Passwords do not match')
