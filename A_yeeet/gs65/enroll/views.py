from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from . froms import SignUpForm, EditUserProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
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

def userlogin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/profile/')
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
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'enroll/userlogin.html', {'form':fm})

def userprofile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = EditUserProfileForm(request.POST, instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'You have changed your informations successfully')
                return HttpResponseRedirect('/profile/')
        else:
            fm = EditUserProfileForm(instance=request.user)
        return render(request, 'enroll/profile.html', {'form' : fm, 'name' : request.user})
    else:
        return HttpResponseRedirect('/login/')
        

def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


# Change password using old password
def userchangepass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Your password has been changed successfully')
                update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'enroll/changepass.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')
        
# Chage password without using old password
def userchangepass1(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Your password has been changed successfully')
                update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect('/profile/')
        else:
            fm = SetPasswordForm(user=request.user)
        return render(request, 'enroll/changepass1.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')
