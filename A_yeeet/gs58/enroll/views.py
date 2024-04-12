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
            print(messages.get_level(request))
            messages.info(request, 'Your account has been created successfully')
            print(messages.get_level(request))
            messages.debug(request, 'This is debug message')
            print(messages.get_level(request))
            
            # as the level is set to debug in this line,
            # the message will be activated from here(not from the previous line where we tried to use debug message)
            messages.set_level(request, messages.DEBUG)
            messages.debug(request, 'This is debug new message')
            print(messages.get_level(request))
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form' : fm})