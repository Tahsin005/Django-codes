from django.shortcuts import render
from . models import Student 

# Create your views here.
def home(request):
    # student_data = Student.objects.get(pk=1)
    
    # student_data = Student.objects.first()
    # student_data = Student.objects.last()
    # student_data = Student.objects.order_by('name').first()
    # student_data = Student.objects.order_by('name').last()
    
    
    # student_data = Student.objects.latest('pass_date')
    # student_data = Student.objects.latest('id')
    # student_data = Student.objects.latest('city')
    # student_data = Student.objects.latest('marks')
    
    
    # student_data = Student.objects.earliest('pass_date')
    # student_data = Student.objects.earliest('id')
    # student_data = Student.objects.earliest('city')
    # student_data = Student.objects.earliest('marks')
    
    # student_data = Student.objects.all()
    # # print(student_data.exists())
    # one_data = Student.objects.get(pk=1)
    # print(student_data.filter(pk=one_data.pk).exists())
    
    
    # student_data = Student.objects.create(name='sameer', roll=111, city='cox', marks=91, pass_date='2024-5-4')
    
    # student_data, created = Student.objects.get_or_create(name='sameer', roll=112, city='cox', marks=91, pass_date='2024-5-4')
    
    # print(student_data, created) 
    
    # student_data = Student.objects.filter(pk=3).update(name='Messi', marks=110)
    # student_data = Student.objects.filter(city='bogra').update(city='Rosario')
    
    
    # student_data, created = Student.objects.update_or_create(id=11, name='sameer', defaults={'name':'Kohli'})
    
    # print(student_data, created) 
    
    # objs = [
    #     Student(name='lilin', roll=113, city='cox', marks=91, pass_date='2024-5-4'),
    #     Student(name='sharar', roll=114, city='cox', marks=91, pass_date='2024-5-4'),
    #     Student(name='arham', roll=115, city='dhaka', marks=91, pass_date='2024-5-4'),
    #     Student(name='yasin', roll=116, city='cox', marks=91, pass_date='2024-5-4'),
    # ]
    # student_data = Student.objects.bulk_create(objs)
    
    # all_student_data = Student.objects.all()
    # for stu in all_student_data:
    #     stu.city = 'Bhel'
    # student_data = Student.objects.bulk_update(all_student_data, ['city'])
    
    # student_data = Student.objects.in_bulk([1, 2])
    # print(student_data[1].name)
    # print(student_data[1].city)
    # student_data = Student.objects.in_bulk()
    # print(student_data[2].name)
    # print(student_data[2].city)
    
    # student_data = Student.objects.get(pk=9)
    # student_data.delete()
    student_data = Student.objects.all()
    print(student_data.count())
    # student_data = Student.objects.count(city='Bhel')
    print('Return : ', student_data)
    return render(request, 'school/home.html', {'student':student_data})