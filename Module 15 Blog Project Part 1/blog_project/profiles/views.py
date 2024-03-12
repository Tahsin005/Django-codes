from django.shortcuts import render, redirect
from profiles.forms import ProfileForm
# Create your views here.
def add_profile(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('add_profile')
    return render(request, 'add_profile.html', {'form': form})