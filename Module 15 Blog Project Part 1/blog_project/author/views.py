from django.shortcuts import render, redirect
from author.forms import AuthorForm
# Create your views here.
def add_author(request):
    form = AuthorForm()
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('add_author')
    return render(request, 'add_author.html', {'form': form})