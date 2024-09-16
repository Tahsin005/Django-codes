from . models import UserRegistration
from django import forms 

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = '__all__'
        
        genders = [{'male', 'Male'}, {'females', 'Female'}]
        countries = [
            ("select", "Please Choose Country"),
            ('Bangladesh', 'Bangladesh'),
            ('USA', 'USA'),
            ('UK', 'UK'),
            ('Germany', 'Germany'),
            ('France', 'France'),
            ('Italy', 'Italy'),
        ]
        
        widgets = {
            'password': forms.PasswordInput(),
            'confirm_password': forms.PasswordInput(),
            'gender': forms.RadioSelect(choices=genders),
            'country': forms.Select(choices=countries),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'email': forms.EmailInput(),
            'website_url': forms.URLInput(),
        }