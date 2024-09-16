from . models import UserRegistration
from django import forms 
import re
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
    # Field level validation
    def clean_phone_number(self):
        iphonenumber = self.cleaned_data.get('phone_number')
        if iphonenumber:
            pattern = re.compile(r"(0|91)?[6-9][0-9]{9}")
            if not re.fullmatch(pattern, iphonenumber):
                raise forms.ValidationError("Invalid Phone Number! Example: 919234567891")
            return iphonenumber
        