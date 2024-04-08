from django.shortcuts import render
from . forms import StudentRegistration
# Create your views here.

def showformdata(request):
    fm = StudentRegistration(initial={'name' : 'This initial value was setted during the runtime'})
    return render(request, 'enroll/userregistration.html', {'form' : fm}) 