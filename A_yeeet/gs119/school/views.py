from django.shortcuts import render
from . models import Student
from django.views.generic.list import ListView
# Create your views here.
class StudentListView(ListView):
    model = Student
    template_name_suffix = '_get'
    # ordering = ['name']
    ordering = ['roll']