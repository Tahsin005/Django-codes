from django.shortcuts import render, redirect
from . forms import RegisterForm, ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# Create your views here.
def home(request):    
    return render(request, './home.html')
def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account created successfully')
                
                form.save(commit=True)
                print (form.cleaned_data)
        else:
            form = RegisterForm()
        return render(request, './signup.html', {'form': form})
    else:
        return redirect('profile')

def userlogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                
                # Check kortesi user database e ase kina
                user = authenticate(username = name, password = userpass)
                
                if user is not None:
                    login(request, user)
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request, './login.html', {'form': form})
    else:
        return redirect('profile')
    
def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserData(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request, 'Account updated successfully')
                
                form.save(commit=True)
                print (form.cleaned_data)
        else:
            form = ChangeUserData(instance=request.user)
        return render(request, './profile.html', {'form': form})
    else:
        return redirect('signup')

def userlogout(request):
    logout(request)
    return redirect('userlogin')

def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, "Password changed.")
                return redirect('profile')
        else:
            form = PasswordChangeForm(request.user)
        return render(request, './passchange.html', {'form': form})
    else:
        return redirect('userlogin')

def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                # messages.success(request, "Password changed.")
                return redirect('profile')
        else:
            form = SetPasswordForm(request.user)
        return render(request, './passchange.html', {'form': form})
    else:
        return redirect('userlogin')
    
def change_user_data(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserData(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request, 'Account updated successfully')
                
                form.save(commit=True)
                print (form.cleaned_data)
        else:
            form = ChangeUserData()
        return render(request, './profile.html', {'form': form})
    else:
        return redirect('signup')