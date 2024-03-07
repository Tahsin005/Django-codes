from django.shortcuts import render
from . forms import contactForm, studentData, passwordValidationProject
# Create your views here.
def home (request):
    return render(request, './first_app/home.html')

def about (request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, './first_app/about.html', {'name': name, 'email': email, 'select': select})
    else:
        return render(request, './first_app/about.html')

def submit_form (request):
    # print(request.POST)
    
    return render(request, './first_app/form.html')

def DjangoForms(request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            # files = form.cleaned_data['files']
            # with open('./first_app/upload/' + files.name, 'wb+') as destination:
            #     for chunk in files.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
            return render (request, './first_app/django_form.html', {'form' : form})
    else:
        form = contactForm()
    return render (request, './first_app/django_form.html', {'form' : form})

def studentForm(request):
    if request.method == 'POST':
        form = studentData(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = studentData()
    return render (request, './first_app/django_form.html', {'form' : form})

def passwordValidation(request):
    if request.method == 'POST':
        form = passwordValidationProject(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = passwordValidationProject()
    return render (request, './first_app/django_form.html', {'form' : form})