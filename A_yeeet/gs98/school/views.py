from django.shortcuts import render
from . models import Student
from datetime import date, time
# Create your views here.
def home(request):
    # student_data = Student.objects.all()
    
    # student_data = Student.objects.filter(name__exact='sonam')
    # student_data = Student.objects.filter(name__iexact='Sonam')
    # student_data = Student.objects.filter(name__contains='a')
    # student_data = Student.objects.filter(name__icontains='A')
    
    # student_data = Student.objects.filter(id__in=[1, 2, 6])
    # student_data = Student.objects.filter(marks__in=[60, 70])
    
    # student_data = Student.objects.filter(marks__gt=60)
    # student_data = Student.objects.filter(marks__gte=60)
    # student_data = Student.objects.filter(marks__lt=60)
    # student_data = Student.objects.filter(marks__lte=60)
    
    # student_data = Student.objects.filter(name__startswith='s')
    # student_data = Student.objects.filter(name__istartswith='S')
    
    # student_data = Student.objects.filter(name__endswith='n')
    # student_data = Student.objects.filter(name__iendswith='N')
    
    # student_data = Student.objects.filter(passdate__range=('2024-04-23', '2024-04-28')) # year - month - day
    
    # student_data = Student.objects.filter(admdatetime__date=date(2024, 4, 23)) 
    # student_data = Student.objects.filter(admdatetime__date__gte=date(2024, 4, 23)) 
    
    
    # student_data = Student.objects.filter(passdate__year=2020) 
    # student_data = Student.objects.filter(passdate__year__gt=2020) 
    # student_data = Student.objects.filter(passdate__month=4) 
    # student_data = Student.objects.filter(passdate__month__gte=4) 
    # student_data = Student.objects.filter(passdate__day=24) 
    # student_data = Student.objects.filter(passdate__day__lte=24) 
    # # Consider 52 weeks a year
    # student_data = Student.objects.filter(passdate__week=24) 
    # student_data = Student.objects.filter(passdate__week__gte=10) 
    
    # student_data = Student.objects.filter(passdate__week_day=3) 
    
    # # 4 quarters a year (3 months each)
    # student_data = Student.objects.filter(passdate__quarter=2) 
    
    student_data = Student.objects.filter(admdatetime__time__gt=time(11,10)) # in 24 hour format
    student_data = Student.objects.filter(admdatetime__hour__gte=11) # 0 to 24
    student_data = Student.objects.filter(admdatetime__minute__gte=14) # 0 to 59
    student_data = Student.objects.filter(admdatetime__second__gte=14) # 0 to 59
    
    print('Return : ', student_data) 
    print()
    print('SQL : ', student_data.query)
    return render(request, 'school/home.html', {'students': student_data})