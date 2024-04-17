from django.shortcuts import render, HttpResponse
from datetime import datetime, timedelta
# Create your views here.
def setsession(request):
    request.session['name'] = 'Sonam'
    return render(request, 'student/setsession.html')

def getsession(request):
    if 'name' in request.session:
        name = request.session['name']
        request.session.modified = True
        return render(request, 'student/getsession.html', {'name': name})
    else:
        return HttpResponse('Your session has been expired')

def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'student/delsession.html')