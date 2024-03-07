from django.shortcuts import render
from . forms import studentData
# Create your views here.
def home(request):
    return render(request, './first_app/home.html')
def about(request):
    return render(request, './first_app/about.html')
def submit_django_form(request):
    if request.method == 'POST':
        form = studentData(request.POST, request.FILES)
        if form.is_valid():
            files = form.cleaned_data['files']
            with open('./first_app/upload/' + files.name, 'wb+') as destination:
                for chunk in files.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
    else:
        form = studentData()
    return render(request, './first_app/django_form.html', {'form' : form})