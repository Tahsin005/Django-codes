from django.shortcuts import render
from . forms import StudentRegistration 
from django.contrib import messages
# Create your views here.
def regi(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            # messages.add_message(request, messages.SUCCESS, 'Your account has been created successfully')
            # messages.add_message(request, messages.INFO, 'Your account has been created successfully')
            # messages.info(request, 'Your account has been created successfully')
            messages.success(request, 'Your account has been created successfully')
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form' : fm})