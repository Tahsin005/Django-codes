from . models import Employee, EmployeeCertificate
from django import forms

class EmployeeForm(forms.ModelForm):
    pan_card_pic_blob = forms.ImageField(required=False)
    class Meta:
        model = Employee
        # fields = ['first_name', 'last_name', 'cv_file', 'photo_file'] 
        fields = '__all__'