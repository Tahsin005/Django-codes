from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d = {'author' : 'Tahsin',
        'age' : 15,
        'lst' : ['Python', 'is', 'best'], 
        'birthday' : datetime.datetime.now(), 
        'val' : '',
        'courses' : [
        {
            'id' : 1, 
            'name' : 'Python',
            'fee' : 6500
        },
        {
            'id' : 2, 
            'name' : 'Django',
            'fee' : 5500

        },
        {
            'id' : 3, 
            'name' : 'Golang',
            'fee' : 2000

        }

    ]}
    return render(request, 'first_app/home.html', context=d)