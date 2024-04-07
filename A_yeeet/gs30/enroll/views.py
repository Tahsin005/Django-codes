from django.shortcuts import render
from . forms import StudentRegistration
# Create your views here.

def showformdata(request):
    fm = StudentRegistration()
    fm.order_fields(field_order=['email', 'first_name', 'name'])
    
    
    # fm = StudentRegistration(auto_id='some_%s')
    
    # to set the field name as id 
    # fm = StudentRegistration(auto_id=True, label_suffix=' ', initial={'name' : 'suiiii', 'email' : 'some_email@gmail.com'})
    
    # a string without format (%s) will act a if it was set to true
    # fm = StudentRegistration(auto_id='tahsin')
    
    # will remove the id completely 
    # fm = StudentRegistration(auto_id=False)
    
    
    return render(request, 'enroll/userregistration.html', {'form' : fm})