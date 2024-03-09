from django.shortcuts import render
from first_app.forms import StudentForm
# Create your views here.
def home(request):
    std = StudentForm()
    return render(request, 'first_app/home.html', {'form' : std})