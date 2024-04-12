from django.shortcuts import render
from . forms import StudentRegistration 
from django.contrib import messages
# Create your views here.
def regi(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.info(request, 'Now you can login')
            messages.success(request, 'Update hoiye gese')
            messages.warning(request, 'This is warning')
            messages.error(request, 'This is an error')
            
            storage = messages.get_messages(request)
            for message in storage:
                print(message)
            
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form' : fm})