from django.shortcuts import render, redirect
from . models import Employee, PartTimeEmployee, OnSiteEmployees, State, City, Country
from . forms import EmployeeForm, PartTimeEmployeeForm, DynamicPartTimeEmployeeForm, PartTimeEmployeeFormSet, OnSiteEmployeesForm

from django.http import JsonResponse

from django.core.paginator import Paginator, PageNotAnInteger
from django.conf import settings
from django.db import transaction
from django.db.models import Q
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
     
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_ids')
        if selected_ids:
            PartTimeEmployee.objects.filter(pk__in=selected_ids).delete()
            return redirect('BDD')
    return render(request, 'PayRollApp/BulkDeleteDemo.html', {'employees': employees})
    
def DeleteUsingRadio(request):
    employees = PartTimeEmployee.objects.all()
    
    if request.method == 'POST':
        selected_id = request.POST.get('selected_id')
        if selected_id:
            PartTimeEmployee.objects.filter(pk=selected_id).delete()
            return redirect('DUR')
        else:
            return redirect('BDD')
    return render(request, 'PayRollApp/DeleteUsingRadio.html', {'employees': employees})
    


def PageWiseEmployeeList(request):
    page_size = int(request.GET.get('page_size', getattr(settings, 'PAGE_SIZE', 5)))
    page = request.GET.get('page', 1)
    
    search_query = request.GET.get('search', '')
    
    sort_by = request.GET.get('sort_by', 'id')
    sort_order = request.GET.get('sort_order', 'asc') 
    
    valid_sort_fields = ['id', 'FirstName', 'LastName', 'TitleName']
    if sort_by not in valid_sort_fields:
        sort_by = 'id' 
    
    employees = PartTimeEmployee.objects.filter(
        Q(id__icontains=search_query) |
        Q(FirstName__icontains=search_query) |
        Q(LastName__icontains=search_query) |
        Q(TitleName__icontains=search_query) 
    )
    
    if sort_order == 'desc':
        employees = employees.order_by(f'-{sort_by}')
    else:
        employees = employees.order_by(sort_by)
    
    # employees = PartTimeEmployee.objects.all()
    
    paginator = Paginator(employees, page_size)
    
    try:
        employees_page = paginator.page(page)
    except PageNotAnInteger:
        employees_page = paginator.page(1)
    
    return render(request, 'PayRollApp/PageWiseEmployees.html', {'employees_page': employees_page, 'page_size': page_size, 'search_query': search_query, 'sort_order': sort_order, 'sort_by': sort_by})




def cascadingSelect(request):
    employee_form = OnSiteEmployeesForm()
    
    if request.method == 'POST':
        employee_form = OnSiteEmployeesForm(request.POST)
        if employee_form.is_valid():
            employee_form.save()
            return JsonResponse({'success': True})
    
    return render(request, 'PayRollApp/CascadingDemo.html', {'employee_form': employee_form})


def load_states(request):
    country_id = request.GET.get('country_id')
    states = State.objects.filter(country_id=country_id).values('id', 'name')
    return JsonResponse(list(states), safe=False)

def load_cities(request):
    state_id = request.GET.get('state_id')
    cities = City.objects.filter(state_id=state_id).values('id', 'name')
    return JsonResponse(list(cities), safe=False)


def TransactionDemo(request):
    try:
        with transaction.atomic():
            employee = PartTimeEmployee.objects.create(FirstName='Naima', LastName='Jannathul', TitleName='Python developer')
            employee = PartTimeEmployee.objects.create(FirstName='petricia', LastName='thorton', TitleName='Python developer')
            employee = PartTimeEmployee.objects.create(FirstName='gini', LastName='thorton', TitleName='Django developer')
            employee = PartTimeEmployee.objects.create(FirstName='sharar', LastName='iram', TitleName='Doctor')
            employee = PartTimeEmployee.objects.create(FirstName='tamim', LastName='tamim', TitleName='Doctor footballer')
    except Exception as e:
        return render(request, 'PayRollApp/TransactionDemo.html', {'Message': str(e)})
    return render(request, 'PayRollApp/TransactionDemo.html', {'Message': 'Success!!'})