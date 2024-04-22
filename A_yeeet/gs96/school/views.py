from django.shortcuts import render
from . models import Student, Teacher
from django.db.models import Q

# Create your views here.
def home(request):
    # student_data = Student.objects.all()
    
    # student_data = Student.objects.filter(marks = 40)
    
    # student_data = Student.objects.exclude(marks = 40)
    
    # student_data = Student.objects.order_by('marks')
    # student_data = Student.objects.order_by('-marks')
    # student_data = Student.objects.order_by('?')
    # student_data = Student.objects.order_by('name')
    
    # student_data = Student.objects.order_by('id').reverse()[:5]
    # student_data = Student.objects.values()
    # student_data = Student.objects.values('name', 'city')
    
    # student_data = Student.objects.values_list()
    # student_data = Student.objects.values_list('id', 'name')
    # student_data = Student.objects.values_list('id', 'name', named=True)
    
    
    # student_data = Student.objects.using('default')
    
    
    # student_data = Student.objects.dates('pass_date', 'week')
    
    
    
    ########################
    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    
    # # student_data = qs2.union(qs1)
    # # student_data = qs2.union(qs1, all=True)
    # # student_data = qs2.intersection(qs1)
    # student_data = qs2.difference(qs1)
    # student_data = qs1.difference(qs2)
    
    
    
    ################################
    # AND OR operator
    # student_data = Student.objects.filter(id=5) & Student.objects.filter(roll=106)
    # student_data = Student.objects.filter(id=5, roll=106)
    # student_data = Student.objects.filter( Q(id=5) & Q(roll=106))
    
     
    student_data = Student.objects.filter(id=6) | Student.objects.filter(roll=106)
    
    print('Return : ', student_data)
    # print("SQL Query : ", student_data.query)
    return render(request, 'school/home.html', {'students':student_data})