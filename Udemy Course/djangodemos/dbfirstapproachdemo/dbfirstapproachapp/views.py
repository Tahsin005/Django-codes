from django.shortcuts import render
from . models import Categories
# Create your views here.
def ShowCategories(request):
    categories = Categories.objects.all()
    
    return render(request, 'dfap/ShowCategories.html', {'categories': categories})