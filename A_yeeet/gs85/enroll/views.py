from django.shortcuts import render
from django.views.decorators.cache import cache_page
# Create your views here.

def home(request):
    return render(request, 'enroll/course.html')
