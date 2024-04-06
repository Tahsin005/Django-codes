from django.shortcuts import render
from enroll.models import Student
# Create your views here.
def studentinfo(request):
    stud = Student.objects.get(pk=3)
    return render(request, 'enroll/studetails.html', {'stu':stud})