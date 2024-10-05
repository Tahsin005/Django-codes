from django.shortcuts import render, redirect
from . forms import EmployeeForm, EmployeeCertificate
from django.contrib import messages
import os
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