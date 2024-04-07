from django.shortcuts import render
from myapp.models import Image
from myapp.forms import ImageForm
# Create your views here.
def home(request):
    form = ImageForm()
    img = Image.objects.all()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request, 'myapp/home.html', {'form': form, 'img': img})