from django.shortcuts import render
from . forms import StudentRegistration
from . models import User
# Create your views here.

def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            
            # For inserting the data
            # reg = User(name=nm, email=em, password=pw)
            # For updating the data
            # reg = User(id=1, name=nm, email=em, password=pw)
            # reg.save()
            
            # For deleting the data
            reg = User(id=2)
            reg.delete()
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form' : fm})