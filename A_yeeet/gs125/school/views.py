from typing import Any
from django.shortcuts import render
from . models import Student
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
# Create your views here.

class StudentListView(ListView):
    model = Student
    
    
class StudentDetailView(DetailView):
    model = Student
    template_name = 'school/student.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['all_student'] = self.model.objects.all().order_by('name')
        return context
    
    