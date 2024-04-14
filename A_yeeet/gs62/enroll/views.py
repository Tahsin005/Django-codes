from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from . froms import SignUpForm
from django.contrib import messages
# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Your account has been created successfully')
    else:
        fm = SignUpForm()
    return render(request, 'enroll/signup.html', {'form': fm})