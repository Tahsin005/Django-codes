from django.shortcuts import render
from . forms import UserRegistrationForm
# Create your views here.

def SignUp(request):
    form = UserRegistrationForm()
    return render(request, "validationsdemoapp/SignUp.html", {'form': form})