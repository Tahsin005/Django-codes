from django.shortcuts import render, redirect
from . forms import RegistrationForm, ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# Create your views here.
def home(request):
    return render(request, './home.html')

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account is created successfully')
                form.save(commit=True)
                print (form.cleaned_data)
        else:
            form = RegistrationForm()
        return render(request, './signup.html', {'form': form})
    else:
        return redirect('profile')

def userlogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userPassword = form.cleaned_data['password']
                
                user = authenticate(username = name, password = userPassword)
                
                if user is not None:
                    login(request, user)
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request, './userlogin.html', {'form': form})
    else:
        return redirect('profile')
def userlogout(request):
    logout(request)
    return redirect('userlogin')

def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserData(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request, 'User data changed successfully')
                form.save(commit=True)
                print (form.cleaned_data)
        else:
            form = ChangeUserData(instance=request.user)
        return render(request, './profile.html', {'form' : form})
    else:
        return redirect('signup')

def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Password changed successfully using the old password')
                return redirect('profile')
        else:
            form = PasswordChangeForm(request.user)
        return render(request, './pass_change.html', {'form' : form})
    else:
        return redirect('userlogin')
    
def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Password changed successfully using the old password')
                return redirect('profile')
        else:
            form = SetPasswordForm(request.user)
        return render(request, './pass_change.html', {'form' : form})
    else:
        return redirect('userlogin')
    