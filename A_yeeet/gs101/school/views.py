from django.shortcuts import render
from . models import Student
from django.db.models import Q
# Create your views here.
def home(request):
    # student_data = Student.objects.all()[:5]
    student_data = Student.objects.all()[5:10]
    student_data = Student.objects.all()[0:10:2]
    student_data = Student.objects.all()[1:10:2]
    
        
    print('Return : ', student_data) 
    print()
    # print('SQL : ', student_data.query)
    return render(request, 'school/home.html', {'students' : student_data})