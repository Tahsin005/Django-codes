from django.shortcuts import render
from . models import Student
from django.db.models import Q
# Create your views here.
def home(request):
    student_data = Student.objects.filter(Q(id=6) & Q(roll=106))
    student_data = Student.objects.filter(Q(id=6) | Q(roll=109))
    student_data = Student.objects.filter(Q(id=6) | ~Q(roll=109))
    student_data = Student.objects.filter(~Q(id=6) & ~Q(roll=109))
    student_data = Student.objects.filter(~Q(id=6) | Q(roll=109))
    
        
    print('Return : ', student_data) 
    print()
    print('SQL : ', student_data.query)
    return render(request, 'school/home.html', {'students' : student_data})