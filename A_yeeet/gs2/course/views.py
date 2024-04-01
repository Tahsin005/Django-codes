from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('<h1>Home Page!</h1>')
def learn_django(request):
    return HttpResponse('<h1>Hello Django!</h1>')
def learn_python(request):
    return HttpResponse('<h1>Hello Python!</h1>')
def learn_var(request):
    a = '<h1>Hello Variable!</h1>'
    return HttpResponse(a)
def learn_math(request):
    a = 10 + 10
    return HttpResponse(a)
def learn_format(request):
    a = 'SUIII'
    return HttpResponse(f'Hello {a}')