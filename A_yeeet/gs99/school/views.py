from django.shortcuts import render
from . models import Student
from datetime import date, time
from django.db.models import Avg, Min, Max, Sum, Count
# Create your views here.
def home(request):
    student_data = Student.objects.all()
    
    average = student_data.aggregate(Avg('marks'))
    sum = student_data.aggregate(Sum('marks'))
    max = student_data.aggregate(Max('marks'))
    min = student_data.aggregate(Min('marks'))
    count = student_data.aggregate(Count('marks'))
    print(average, sum, max, min, max, count)
    
    context = {
        'students': student_data,
        'average': average,
        'count': count,
        'min': min,
        'max': max,
        'sum': sum,
    }
    
    print('Return : ', student_data) 
    print()
    print('SQL : ', student_data.query)
    return render(request, 'school/home.html', context)