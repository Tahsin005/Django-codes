from django.shortcuts import render
from . forms import UserRegistrationForm
# Create your views here.

def SignUp(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # form.save()
            return render(request, "validationsdemoapp/Home.html")
    return render(request, "validationsdemoapp/SignUp.html", {'form': form})