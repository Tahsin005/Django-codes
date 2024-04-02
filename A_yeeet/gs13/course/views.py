from django.shortcuts import render
from datetime import datetime
# Create your views here.
def learn_django(request):
    d = datetime.now()
    # student = {
    #     'names': ['tahsin', 'ferdous', 'niloy', 'mahin', 'rean', 'ridu', 'rizu']
    # }
    stu = {
        'stu1' : {'name': 'tahsin', 'roll' : 101},
        'stu2' : {'name': 'ferdous', 'roll' : 102},
        'stu3' : {'name': 'aziz', 'roll' : 103},
    }
    students = {'student' : stu}
    # return render(request, 'course/courseone.html', {'nm': 'django is awesome', 'd': d, 'p1': 56.24321, 'p2':56.000, 'p3':56.37000, 'name' : False, 'st': 5})
    return render(request, 'course/courseone.html', students)