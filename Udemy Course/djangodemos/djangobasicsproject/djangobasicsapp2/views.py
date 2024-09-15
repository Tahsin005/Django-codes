from django.shortcuts import render

# Create your views here.
def Home(request):
    templatefilename = "djangobasicsapp2/Home.html"
    return render(request, templatefilename)