from django.shortcuts import render, redirect
from . models import Employee, PartTimeEmployee
from . forms import EmployeeForm, PartTimeEmployeeForm, DynamicPartTimeEmployeeForm, PartTimeEmployeeFormSet
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






def BulkInsertDemo(request):
    extra_forms = 10
    forms = [PartTimeEmployeeForm(request.POST or None, prefix=f'employee-{i}') for i in range(extra_forms)]
    Status = ""
    if request.method == 'POST':
        for form in forms:
            if form.is_valid() and form.cleaned_data.get('FirstName', ''):
                form.save()
                Status = "Part Time Employees inserted successfully."
    return render(request, 'PayRollApp/parttimeemployee_list.html', {'forms': forms, 'extra_forms': range(extra_forms), 'Status': Status})


def NewBulkInsertDemo(request):
    
    if request.method == 'POST':
        formset = PartTimeEmployeeFormSet(request.POST, prefix="employee")
        if formset.is_valid():
            employees = formset.save(commit=False)
            PartTimeEmployee.objects.bulk_create(employees)
            return redirect('NBID')
    else:
        formset = PartTimeEmployeeFormSet(queryset=PartTimeEmployee.objects.none(), prefix="employee")
    return render(request, 'PayRollApp/NewBulkInsert.html', {'formset': formset})


def BulkUpdationDemo(request):
    employees = PartTimeEmployee.objects.all()
    forms = [PartTimeEmployeeForm(request.POST or None, instance=employee, prefix=f'employee-{employee.id}') for employee in employees]
    
    if request.method == 'POST':
        updated_data = []
        for form in forms:
            if form.is_valid():
                employee = form.instance
                employee.FirstName = form.cleaned_data['FirstName']
                employee.LastName = form.cleaned_data['LastName']
                employee.TitleName = form.cleaned_data['TitleName']
                updated_data.append(employee)
        PartTimeEmployee.objects.bulk_update(updated_data, ['FirstName', 'LastName', 'TitleName']) 
    
    return render(request, 'PayRollApp/BulkUpdationDemo.html', {'forms': forms, 'employees': employees})

def BulkDeleteDemo(request):
    employees = PartTimeEmployee.objects.all()
    return render(request, 'PayRollApp/BulkDeleteDemo.html', {'employees': employees})
    