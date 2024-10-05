from django.shortcuts import render
from . forms import EmployeeForm
# Create your views here.

def employee_create(request):
    employee_form = EmployeeForm()
    
    return render(request, 'uploadfilesapp/employee_create.html', {'employee_form': employee_form})