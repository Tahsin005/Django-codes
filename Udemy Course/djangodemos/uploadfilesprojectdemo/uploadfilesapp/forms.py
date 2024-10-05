from . models import Employee, EmployeeCertificate
from django import forms

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'cv_file', 'photo_file'] 