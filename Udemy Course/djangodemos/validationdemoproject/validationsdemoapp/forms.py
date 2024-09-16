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
    
    # Form level validation
    def clean(self):
        cleaned_data = super().clean()
        
        ipassword = cleaned_data.get('password')
        iconfirm_password = cleaned_data.get('confirm_password')
        
        if ipassword and iconfirm_password:
            if ipassword != iconfirm_password:
                raise forms.ValidationError("Passwords do not match!")
        
        iusername = cleaned_data.get('username')
        if iusername:
            if ipassword == iusername:
                raise forms.ValidationError("Username should not be same as password!")
        
        icountry = cleaned_data.get('country')
        if icountry == "select":
            raise forms.ValidationError("Please choose a country!")
        
        iterms_conditions = cleaned_data.get('terms_conditions')
        if not iterms_conditions:
            raise forms.ValidationError("You must agree to terms and conditions!")
        
        return cleaned_data