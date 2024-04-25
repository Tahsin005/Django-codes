from django.shortcuts import render
from . models import Student
from django.views.generic.list import ListView
# Create your views here.
class StudentListView(ListView):
    model = Student
    template_name = 'school/student.html'
    context_object_name = 'students'