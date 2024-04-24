from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

def myview(request):
    return HttpResponse('<h1>Function based view</h1>')


class MyView(View):
    name = 'sonam'
    def get(self, request):
        # return HttpResponse('<h1>Class based view - GET</h1>')
        return HttpResponse(self.name)
    
class MyViewChild(MyView):
    def get(self, request):
        return HttpResponse(self.name)