from django.shortcuts import render
from django.http import HttpResponseRedirect
from . forms import StudentRegistration
# Create your views here.

def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print('Cleaned data')
            print('Name : ', fm.cleaned_data['name'])
            print('Agree : ', fm.cleaned_data['agree'])
            print('Roll : ', fm.cleaned_data['roll'])
            print('Price : ', fm.cleaned_data['price'])
            print('Rate : ', fm.cleaned_data['rate'])
            print('Comment : ', fm.cleaned_data['comment'])
            print('Email : ', fm.cleaned_data['email'])
            print('Password : ', fm.cleaned_data['password'])
            print('website : ', fm.cleaned_data['website'])
            print('Description : ', fm.cleaned_data['description'])
            print('Notes : ', fm.cleaned_data['notes'])
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form' : fm})   