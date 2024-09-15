from django.shortcuts import render, redirect
from . models import Employee
from . forms import EmployeeForm
# Create your views here.
def EmployeesList(request):
    Employees = Employee.objects.all()
    # Employees = Employee.objects.select_related('EmpDepartment', 'EmpCountry').all()
    print(Employees.query)
    TemplateFile = 'PayRollApp/EmployeesList.html'
    Dict = {
        'Employees': Employees,
    }
    return render(request, TemplateFile, Dict)


def EmployeeDetails(request, id):
    TemplateFileName = 'PayRollApp/EmployeesDetails.html'
    # employee = Employee.objects.get(id=id)
    # Dict = {
    #     'Employee': employee
    # }
    employee = Employee.objects.select_related('EmpDepartment', 'EmpCountry').all().filter(id=id)
    Dict = {
        'Employee': employee[0]
    }
    
    return render(request, TemplateFileName, Dict)

def EmplyeeDelete(request, id):
    TemplateFileName = 'PayRollApp/EmployeeDelete.html'
    # employee = Employee.objects.get(id=id)
    # Dict = {
    #     'Employee': employee
    # }
    employee = Employee.objects.select_related('EmpDepartment', 'EmpCountry').all().filter(id=id)
    Dict = {
        'Employee': employee[0]
    }
    if (request.method == 'POST'):
        employee.delete()  
        return redirect('EmployeesList')
    return render(request, TemplateFileName, Dict) 

def EmployeeUpdate(request, id):
    TemplateFileName = 'PayRollApp/EmployeeUpdate.html'
    # employee = Employee.objects.get(id=id)
    employee = Employee.objects.select_related('EmpDepartment', 'EmpCountry').all().filter(id=id)
    form = EmployeeForm(instance=employee[0])
    Dict = {
        'form': form
    }
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee[0])
        if form.is_valid():
            form.save()
            return redirect('EmployeesList')
    
    return render(request, TemplateFileName, Dict)  

def EmployeeInsert(request):
    TemplateFileName = 'PayRollApp/EmployeeInsert.html'
    form = EmployeeForm()
    Dict = {
        'form': form
    }
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('EmployeesList')
    
    return render(request, TemplateFileName, Dict)