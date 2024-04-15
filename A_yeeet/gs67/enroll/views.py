from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from . froms import SignUpForm, EditUserProfileForm, EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User, Group
# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Your account has been created successfully')
            user = fm.save()
            group = Group.objects.get(name='Editor')
            user.groups.add(group)
    else:
        fm = SignUpForm()
    return render(request, 'enroll/signup.html', {'form': fm})

def userlogin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard/')
    else:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully')
                    return HttpResponseRedirect('/dashboard/')
        else:
            fm = AuthenticationForm()
        return render(request, 'enroll/userlogin.html', {'form':fm})

def userdashboard(request):
    if request.user.is_authenticated:
        return render(request, 'enroll/dashboard.html', {'name' : request.user.username})
    else:
        return HttpResponseRedirect('/login/')
        

def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

