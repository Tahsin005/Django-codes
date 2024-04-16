from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.
def setsession(request):
    request.session['name'] = 'Sonam'
    request.session['lname'] = 'Kumari'
    
    return render(request, 'student/setsession.html')

def getsession(request):
    # name = request.session['name']
    name = request.session.get('name', default='Anonymous')
    lname = request.session.get('lname', default='user')
    return render(request, 'student/getsession.html', {'name': name, 'lname': lname})

def delsession(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request, 'student/delsession.html')