from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse
# Create your views here.
def home(request):
    print('I am home view')
    return HttpResponse('This is home page')

def excp(request):
    print('I am exception view')
    a = 10 / 0
    return HttpResponse('This is exception page')

def user_info(request):
    print('I am user info view')
    context = {
        'name' : 'Tahsin',
    }
    return TemplateResponse(request, 'blog/user.html', context)