from django.shortcuts import render
from . import models
# Create your views here.
def home(request):
    student = models.Student.objects.all()
    print(student)
    return render(request, 'first_app/home.html', {'data' : student})