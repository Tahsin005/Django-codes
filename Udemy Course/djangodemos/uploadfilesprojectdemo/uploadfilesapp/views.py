from django.shortcuts import render, redirect
from . forms import EmployeeForm
from . models import EmployeeCertificate, Employee
from django.contrib import messages
import os
import base64
from django.shortcuts import get_object_or_404, redirect, render
# Create your views here.

def employee_create(request):
    employee_form = EmployeeForm()
    
    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST, request.FILES)
        certificate_files = request.FILES.getlist('certificate_files')
        
        if employee_form.is_valid():
            employee = employee_form.save()
            if len(certificate_files) > 10:
                messages.error(request, 'You can upload a maximum of 10 certificate files')
                return redirect('employee_create')
            
            employee_folder = os.path.join('employee_files', 'certificates', str(employee.id))
            os.makedirs(employee_folder, exist_ok=True)
            
            for idx, certificate_file in enumerate(certificate_files, start=1):
                original_extension = os.path.splitext(certificate_file.name)[1]

                # Rename and save the certificate file with the desired format
                new_filename = f'{employee.id}_{employee.first_name}_{idx}{original_extension}'
                new_file_path = os.path.join(employee_folder, new_filename)

                # Save the certificate file
                with open(new_file_path, 'wb+') as destination:
                    for chunk in certificate_file.chunks():
                        destination.write(chunk)
                
                EmployeeCertificate.objects.create(
                    employee=employee,
                    certificate_file=new_file_path,  # Save the path, not the File object
                )           
    
    return render(request, 'uploadfilesapp/employee_create.html', {'employee_form': employee_form})


def employee_list(request):
    employees = Employee.objects.all()
    
    employee_data = []
    for employee in employees:
        existing_certificates = len(EmployeeCertificate.objects.filter(employee=employee))
        remaing_certificates = 10 - existing_certificates
        employee_data.append({
            'employee': employee,
            'remaining_certificates': remaing_certificates
        })
    return render(request, 'uploadfilesapp/employee_list.html', {'employee_data': employee_data})



def employee_details(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    certificates = EmployeeCertificate.objects.filter(employee=employee)

    # Convert the binary image data to base64
    pan_card_pic_base64 = base64.b64encode(employee.pan_card_pic_blob).decode('utf-8') if employee.pan_card_pic_blob else None

    #return render(request, 'uploadfilesapp/employee_details.html', 
                  #{'employee': employee, 'certificates': certificates})
    
    return render(request, 'uploadfilesapp/employee_details.html', 
                  {'employee': employee, 
                   'pan_card_pic_base64': pan_card_pic_base64, 
                   'certificates': certificates})