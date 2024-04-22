from django.shortcuts import render

# Create your views here.
def home(request):
    print('I am from home view')
    return render(request, 'mysite/home.html')

def about(request):
    print('I am from about view')
    return render(request, 'mysite/about.html')