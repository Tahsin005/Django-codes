from django import forms
from . models import Employee, PartTimeEmployee, OnSiteEmployees

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        
        widgets = {
            'BirthDate': forms.widgets.DateInput(attrs={'type': 'date'}),
            'HireDate': forms.widgets.DateInput(attrs={'type': 'date'}),
        }
        
PartTimeEmployeeForm = forms.modelform_factory(PartTimeEmployee, fields=['FirstName', 'LastName', 'TitleName'])

class DynamicPartTimeEmployeeForm(PartTimeEmployeeForm):
    def __init__(self, *args, **kwargs):
        super(DynamicPartTimeEmployeeForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.pop("required", None)
            
            
            
class NewPartTimeEmployeeForm(forms.ModelForm):
    class Meta:
        model = PartTimeEmployee
        fields = '__all__'
        
PartTimeEmployeeFormSet = forms.modelformset_factory(PartTimeEmployee, form=NewPartTimeEmployeeForm, extra=10)



class OnSiteEmployeesForm(forms.ModelForm):
    class Meta:
        model = OnSiteEmployees
        fields = ['first_name', 'last_name', 'country', 'state', 'city']
        
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'Last Name'
            }),
            'country': forms.Select(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'Country'
            }), 
            'state': forms.Select(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'State'
            }),
            'city': forms.Select(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'City'
            }),
        }