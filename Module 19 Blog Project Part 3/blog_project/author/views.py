from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from author.forms import RegistrationForm, ChangeUserForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post
from django.contrib.auth.views import LoginView, LogoutView

from django.views.generic import UpdateView
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Registration successful')
            return redirect('register')
    else:
        register_form = RegistrationForm()
    return render(request,'register.html', {'form': register_form, 'type' : 'Register'})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('profile')
            else:
                messages.warning(request, 'Login information is incorrect')
                return redirect('login')
    else:
        form = AuthenticationForm()
    return render(request, 'register.html', {'form': form, 'type' : 'Login'})


class UserLoginView(LoginView):
    template_name = 'register.html'
    
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in successfully')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context

@login_required            
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('user_login')

class UserLogoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('user_login')
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.success(request, 'Logged out successfully')
        return response
@login_required            
def profile(request):
    data = Post.objects.filter(author = request.user)
    return render(request,'profile.html' , {'data': data})

@login_required            
def edit_profile(request):
    if request.method == 'POST':
        profile_form = ChangeUserForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
    else:
        profile_form = ChangeUserForm(instance=request.user)
    return render(request,'update_profile.html', {'form': profile_form})

# Edit profile using login view
class EditProfileView(UpdateView):
    form_class = ChangeUserForm
    template_name = 'update_profile.html'
    success_url = reverse_lazy('profile')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@login_required            
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Password changed successfully')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'pass_change.html', {'form': form})

