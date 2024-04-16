from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.
def setsession(request):
    request.session['name'] = 'Sonam'
    request.session['lname'] = 'Jha'
    
    return render(request, 'student/setsession.html')

def getsession(request):
    # name = request.session['name']
    name = request.session.get('name', default='Anonymous')
    keys = request.session.keys()
    items = request.session.items()
    # age = request.session.setdefault('age', '22')
    return render(request, 'student/getsession.html', {'name': name, 'keys': keys, 'items': items})

def delsession(request):
    request.session.flush()
    return render(request, 'student/delsession.html')